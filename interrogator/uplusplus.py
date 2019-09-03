# uplusplus

TRACE = 0
GCBAD = 0
REFC = {}


def djb2(s):
    hash = 5381
    for x in s:
        hash = ((hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF


import ffi
import sys


class cstructs(dict):
    pool = []

    decl = []

    def __init__(self):
        self.ct = dict()
        self.ref = dict()
        self.jit = dict()

    def register(self, cname, lname, lib):
        self.name = "{0}::{1}".format(lname, cname)
        self.lib = ffi.open(lib)
        return self

    def link(self, cls):
        del self.lib
        self.factory = cls
        if cls.__name__ in self.decl:
            slot = self.decl.index(cls.__name__)
            self.decl[slot] = cls
            print("c++", cls.__name__, "found and avail. as Python return type")
        self.__class__.pool.append(self)


class cplusplus:

    # c++ ctor/dtor

    def __init__(self, *argv, **kw):
        global GCBAD, REFC
        c = self.__class__.c
        iref = kw.pop('iptr', None)
        cref = kw.pop('cptr', None)
        if iref or cref:
            # extract pointer addr from source
            if isinstance(iref, cplusplus):
                cref = c.ref[id(iref)]

            # add the cref to class handler for this instance
            c.ref[id(self)] = cref
            REFC.setdefault(cref, 1)
            REFC[cref] += 1
        else:
            GCBAD += 1
            kw['hint'] = 'ctor'
            c.ref[id(self)] = self.__cplusplus_s(c.ct['ctor'], *argv, **kw)

    # ffi call interface 2 types of calls   f(this, ...)  f( ... )


    def __proto_mismatch(self,attr):
        te = TypeError("%s->%s : wrong count of positional arguments" % (self.__class__.__name__,attr) )
        print("ERROR",te,file=sys.stderr)

        c = self.__class__.c
        print("Possible candidate for %s->%s are :" % (self.__class__,attr), file=sys.stderr)
        proto = c.ct.get(attr, None)
        if not isinstance(proto, dict):
            proto = {'*': proto}
        for argc, decl in proto.items():
            print('    %s : %s' % (argc, decl), file=sys.stderr)
        return te


    # instance methods
    def __cplusplus_d(self, call, *argv, **kw):

        if isinstance(call, dict):
            try:
                # get the matching variadic call if any
                call = call.get(1+len(argv), None)

            except Exception as e:
                print(e, ffi_name, len(argv), call, 'argv=', argv)
                raise
        # make it mutable
        argv = list(argv)

        # TODO: debug flag for type checking

        # convert call stack to raw pointer to C structs
        for idx, arg in enumerate(argv):
            if isinstance(arg, cplusplus):
                try:
                    argv[idx] = arg.__class__.c.ref[id(arg)]
                except KeyError:
                    print("arg[%s]=" % idx, arg, "dangling ptr", id(arg), arg.__class__.c.ref)
                    raise
        if call:
            c = self.__class__.c
            ftype, rtype, func = call
            try:
                return func(c.ref[id(self)], *argv)
            except KeyError:
                print(kw, ftype, rtype, func, "dangling ptr", id(self), c.ref)
                raise

        raise self.__proto_mismatch( kw.get('hint', '?jit?') )


    # classmethod (static)
    def __cplusplus_s(self, call, *argv, **kw):

        if isinstance(call, dict):
            try:
                # get the matching variadic call if any
                call = call.get(len(argv), None)

            except Exception as e:
                print(e, ffi_name, len(argv), call, 'argv=', argv)
                raise
        # make it mutable
        argv = list(argv)

        # TODO: debug flag for type checking

        # convert call stack to raw pointer to C structs
        for idx, arg in enumerate(argv):
            if isinstance(arg, cplusplus):
                try:
                    argv[idx] = arg.__class__.c.ref[id(arg)]
                except KeyError:
                    print("arg[%s]=" % idx, arg, "dangling ptr", id(arg), arg.__class__.c.ref)
                    raise
        if call:
            c = self.__class__.c
            ftype, rtype, func = call
            return func(*argv)

        raise self.__proto_mismatch( kw.get('hint', '?jit?') )

    # python interface

    def __repr__(self):
        c = self.__class__.c
        return '<{0} *>({1}#{2})'.format(c.name, c.ref[id(self)], self.refcount())

    def __jit(self, c, attr, *args, **kw):
        global TRACE

        call = c.ct.get(attr, None)
        if not isinstance(call, dict):
            if TRACE:
                print('TRACE', "jit direct", call)
            call = {'*': call}

        k = list(call.keys())
        k.sort()

        ct = None
        rt = None

        for key in k:
            proto = call[key]

            if TRACE:
                print('TRACE', "jit (...) *", key, proto)

            if ct and proto[0] != ct:
                raise Error("174: can't mix static/class and instance method calls on same attribute %s" % attr)
            ct = proto[0]

            if rt and proto[1] != rt:
                raise Error("177: can't mix return types on same attribute %s %s!=%s" % (attr, rt, proto[1]))
            rt = proto[1]

        if ct == 's':
            inline = self.__cplusplus_s
        if ct == 'd':
            inline = self.__cplusplus_d

        # reduce call table if possible
        if call.get('*'):
            call = call['*']

        # can we return a wrapped C++ type ?
        if isinstance(rt, int) and not isinstance(c.decl[rt], str):
            rt = c.decl[rt]

            def jit(*argv, **kw):
                kw['hint'] = attr
                return rt(cptr=inline(call, *argv, **kw))

        else:
            # return raw pointer
            def jit(*argv, **kw):
                kw['hint'] = attr
                return inline(call, *argv, **kw)

        return jit

    def __call(self, attr):
        global TRACE
        c = self.__class__.c
        if attr[0] != '_':
            if TRACE:
                return self.__jit(c, attr)

            hsum = '%s-%s' % (hash(attr), attr)  # should use djb2 to get cross interpreter
            jit = c.get(hsum, None)
            if jit is None:
                jit = self.__jit(c, attr)
                c[hsum] = jit
            return jit
        raise AttributeError("'{0}' C++ class has no method '{1}'".format(c.name, attr))

    # forced gc

    @classmethod
    def destroy(cls, self):
        global GCBAD, REFC
        c = cls.c
        cref = c.ref[id(self)]

        for attr in dir(self):
            try:
                if attr not in ('c', '__del__'):
                    delattr(self, attr)
            except:
                pass

        nref = self.refcount()
        if nref > 1:
            REFC[cref] -= 1
            print("still", nref - 1, "ref. on", cref)
            return
        print("__del__", cref)
        GCBAD -= 1
        try:
            c.ct['dtor'][2](cref)
        finally:
            c.ref.pop(id(self), None)

    def __enter__(self, *argv, **kw):
        return self

    # self.__del__() is not called ...
    def __exit__(self, *argv, **kw):
        global REFC
        self.__class__.destroy(self)

    def refcount(self):
        global REFC
        return REFC.get(self.__class__.c.ref[id(self)], 1)


def noop(*args, **kw):
    pass


def gc():
    global GCBAD, REFC
    import gc

    gc.collect()

    gc.collect()  # one more it's free !
    print("REFS", GCBAD, "ptr=", REFC)
    if GCBAD:
        print(" ----------- Bad GC ------------")  # who said free ?

    for c in cstructs.pool:
        items = []
        for item in c.ref.values():
            if not item in items:
                items.append(item)

        c.ref.clear()
        while items:
            item = items.pop()
            print(c.factory, 'dangling ptr', item)
            c.ct.get('dtor', ['', '', noop])[2](item)

    # luckily we have the pointers left in cstructs of each classes


#
