# uplusplus

TRACE = 0
GCBAD = 0
REFC = {}

FFI_TRACK = {}


def djb2(s):
    hash = 5381
    for x in s:
        hash = ((hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF


import ffi
import sys

DBG = 0


class nullptr(Exception):
    pass


# this is not hashable
nullptr = Exception('NPE')


IDX_CT = const(0)
IDX_RET = const(1)
IDX_ARGC = const(2)
IDX_FFI = const(3)
IDX_KW = const(4)


def passthrough(**kw):
    if TRACE:
        print("  JIT PT", kw.get('cptr'))
    return kw.get('cptr')


def cxx_stack(*argv, **kw):
    argv = list(argv)
    for idx, arg in enumerate(argv):
        if isinstance(arg, cplusplus):
            argv[idx] = arg.__class__.c.ref[id(arg)]

    return argv, kw


def wrap(call, rt, argv, kw, instance=None):
    if TRACE:
        print("  wrap", 'instance=', instance, argv, kw)

    if instance is None:
        argv, kw = cxx_stack(*argv, **kw)
        jt = '  JIT-s'
    else:
        argv, kw = cxx_stack(instance, *argv, **kw)
        jt = '  JIT-d'

    rv = call(*argv)
    print(jt, 'CPTR rv=', rv)
    rv = rt(cptr=rv)
    print(jt, 'PTYPE(%s) rv=' % rt, rv)
    return rv


def call1(ancestor, cls, instance, attr, decl):
    c = cls.c

    ct = decl[IDX_CT]
    rt = decl[IDX_RET]

    argc = decl[IDX_ARGC]

    if isinstance(rt, int):
        if TRACE:
            print("   JIT-1",rt,c.decl[rt])
        rt = c.decl[rt]
    else:
        if TRACE:
            print("   JIT-1 passthrough")
        rt = passthrough

    # OPTIM
    # for TRACE
    ffi = c.get('%s-ffi'%attr,None)
    if ffi is None:
        ffi = ancestor.c.lib.func(*decl[IDX_FFI])
        c['%s-ffi'%attr] = ffi

    # no TRACE
    # ffi = ancestor.c.lib.func(*decl[IDX_FFI])

    # basic/complex return types can be optimized

    # no call stack could be optimized via direct function pointer call

    # kw could be used to pass runtime jit info

    # if not instance(rt,int):
    if DBG:
        print(" -> DIRECT for %s->%s calltype=%s" % (c.name, attr, ct))

        if ct == 's':
            instance = None
        def jit(*argv, **kw):
            return wrap(ffi, rt, argv, kw, instance)

        return jit

    # static call , hide instance if any
    if ct == 's':
        instance = None
        def jit1(*argv, **kw):
            argv, kw = cxx_stack(*argv, **kw)
            if TRACE:
                print("   JIT-1-%s" % ct, argv, FFI_TRACK[id(ffi)])
            return rt(cptr=ffi(*argv))
    else:
        # check nullptr ?
        def jit1(*argv, **kw):
            if TRACE:
                print("   JIT-1-this", argv)
            argv, kw = cxx_stack(instance, *argv, **kw)
            if TRACE:
                print("   JIT-1a-this", argv)

            argv, kw = cxx_stack(*argv, **kw)
            if TRACE:
                print("   JIT-1b-%s" % instance, argv, FFI_TRACK[id(ffi)])
            return rt(cptr=ffi(*argv))


    FFI_TRACK[id(ffi)] = decl
    ancestor.c[attr] = jit1

    # alias to parent so child can call directly next time
    if instance and (ancestor is not cls):
        c[attr] = jit1

    return jit1


# need *HUGE* optim


def get_match(ancestor, cls, rt, ct, pl, argc):
    cando = []
    for proto in pl:
        if ct != proto[IDX_CT]:
            continue

        if argc < proto[IDX_ARGC]:
            break
        elif argc == proto[IDX_ARGC]:
            if TRACE:
                print("   argc=%d for" %argc, proto)
            cando.append(proto)
    return cando


def callx(ancestor, cls, instance, rt, ct, pl, attr, argc, argv, kw):
    global TRACE
    #
    sigkey = '{}-{}'.format(attr, argc)
    #

    if DBG:
        print('  JIT-x CACHING', sigkey, argc)

    cl = []
    for proto in get_match(ancestor, cls, rt, ct, pl, argc):
        ffi = ancestor.c.lib.func(*proto[IDX_FFI])
        FFI_TRACK[id(ffi)] = proto[IDX_FFI]
        cl.append([ffi, proto[IDX_KW]])

    if not len(cl):
        raise TypeError("%s->%s : no match for arguments count" % (ancestor.__name__, attr))

    if len(cl) > 1:
        print("\n  JIT-x ERROR N/I call sig dependant proto")
        print("  ========================================")
        last=TRACE
        TRACE=1
        get_match(ancestor, cls, rt, ct, pl, argc)
        TRACE=last
        print()


    cl = cl[-1][0]

    if instance:
        def jit_n(*argv, **kw):
            if TRACE:
                print("   JIT[%d]-%s" % (argc,ct), argv, FFI_TRACK[id(cl)])

            argv, kw = cxx_stack(instance, *argv, **kw)
            return rt(cptr=cl(*argv))

    else:
        def jit_n(*argv, **kw):
            if TRACE:
                print("   JIT[%d]-%s" % (argc, ct), argv, FFI_TRACK[id(cl)])

            argv, kw = cxx_stack(*argv, **kw)
            return rt(cptr=cl(*argv))


    ancestor.c[sigkey] = jit_n

    # alias to parent so child can call directly next time
    cls.c[sigkey] = jit_n

    return rt(cptr=jit_n(*argv,**kw))



def jit_table(cls, instance, attr):
    global TRACE

    mro = [instance]

    if instance is None:
        mro.append(cls)

    mro.extend(cls.c.bases)  # TODO: recurse ?

    if DBG:
        print("inspecting", mro)

    # maybe self maybe not
    for call_ancestor, ancestor in enumerate(mro):

        # static call don't pass instance so skip and go "call_ancestor==True"
        if not ancestor:
            continue

        c = ancestor.c

        call = c.ct.get(attr, None)
        if not call:
            if TRACE:
                print(" -> no match for %s->%s from %s" % (c.name, attr, cls.c.name))
            continue


        # reduce table to direct call if only 1 choice
        if len(call) == 1:
            return call1(ancestor, cls, instance, attr, call[0])

        if TRACE:
            print(" -> call table for %s->%s from %s" % (c.name, attr, cls.c.name))

        # else build a dynamic proto list candidate table
        rt = ct = None
        pl = []
        for decl in call:
            pl.append(list(decl))
            nct = pl[-1][IDX_CT]
            if ct and (ct != nct):
                raise Exception("174: can't mix static/class and instance method calls on same attribute %s" % attr)
            ct = nct

            nrt = pl[-1][IDX_RET]
            if rt and (rt != nrt):
                raise Exception("177: won't allow mixing return types on same attribute %s %s!=%s" % (attr, rt, nrt))
            rt = nrt

        # do not convert to py class when ctor since raw c pointer will be stored by __init__
        if isinstance(rt, int) and (attr != 'ctor'):
            rt = cls.c.decl[rt]
        else:
            rt = passthrough

        del nrt, nct

        # sort by positional args count to exit faster from table loop
        pl.sort(key=lambda x: x[IDX_ARGC])


        if ct == 's':
            instance = None

            def jit_x(*argv, **kw):
                argc = len(argv) + len(kw)
                sigkey = '{}-{}'.format(attr, argc)
                cl = cls.c.get(sigkey, None)
                if cl:
                    return cl(*argv,**kw)
                if DBG:
                    print("JIT-x INIT[%s-%d] %s->%s(%s) -> %s" % (ct, argc, ancestor, attr, instance, rt), argv, kw)
                return callx(ancestor, cls, instance, rt, ct, pl, attr, argc, argv, kw)
        else:
            def jit_x(*argv, **kw):
                argc = len(argv) + len(kw) # +1
                sigkey = '{}-{}'.format(attr, argc)
                cl = instance.c.get(sigkey, None)
                if cl:
                    return cl(*argv,**kw)
                if DBG:
                    print("JIT-x INIT[%s-%d] %s->%s(%s) -> %s" % (ct,argc, ancestor, attr, instance, rt), argv, kw)
                return callx(ancestor, cls, instance, rt, ct, pl, attr, argc, argv, kw)

        return jit_x

    raise Exception("%s->%s not found" % (mro, attr))


class cstructs(dict):

    lib = None

    pool = []

    decl = []

    bases = []

    def __init__(self):
        self.ct = dict()
        self.ref = dict()
        self.jit = dict()

    def register(self, cname, lname, lib):
        self.name = "{0}::{1}".format(lname, cname)
        if self.__class__.lib is None:
            self.__class__.lib = ffi.open(lib)
        #            if DBG:
        #                print("loading Cni lib %s" % lib)
        return self

    def link(self, cls):
        # del self.lib
        self.factory = cls
        if cls.__name__ in self.decl:
            slot = self.decl.index(cls.__name__)
            self.decl[slot] = cls
            if DBG:
                print("c++", cls.__name__, "found and avail. as Python return type")
        self.__class__.pool.append(self)

    def call(self, cls, attr, instance=None):
        global TRACE
        c = cls.c
        try:
            # how to get cross interpreter to match instances ?
            hsum = '%s-%s' % (id(self), attr)
            jit = self.get(hsum, None)
            # OPTIM
            if jit is None or TRACE:
                jit = jit_table(cls, instance, attr)
                c[hsum] = jit

            return jit

        except Exception as e:
            sys.print_exception(e, sys.stdout)
            raise Exception("%s->%s jit compilation failed" % (c.name, attr))

        if instance:
            raise AttributeError("'{0}' C++ class has no method '{1}'".format(c.name, attr))
        raise AttributeError("'{0}->{1}' is not a C++ static".format(c.name, attr))


class cplusplus:

    # c++ ctor/dtor

    # ffi call interface 2 types of calls   f(this, ...)  f( ... )

    def __init__(self, *argv, **kw):
        global GCBAD, REFC
        c = self.__class__.c
        iref = kw.pop('iptr', None)
        cref = kw.pop('cptr', None)
        if iref or cref:
            # extract pointer addr from source
            if not isinstance(cref, int):
                print("ERROR cref is not a raw pointer but a ",cref)
                iref=cref

            if isinstance(iref, cplusplus):
                if iref.__class__ is not self.__class__:
                    print("cannot do link %s on different type %s" % (iref.__class__,self.__class__) )
                cref = c.ref[id(iref)]

            # add the cref to class handler for this instance
            c.ref[id(self)] = cref
            REFC.setdefault(cref, 1)
            REFC[cref] += 1
            if TRACE:
                print("   ATTACH",iref,cref,'=>',self)
        else:
            GCBAD += 1
            ctor = jit_table(self.__class__, None, 'ctor')
            c.ref[id(self)] = ctor(*argv, **kw)

    # python interface

    def __repr__(self):
        c = self.__class__.c
        try:
            return '<{0} *>({1}#{2})'.format(c.name, c.ref[id(self)], self.refcount())
        except KeyError:
            return '<{0} *>'.format(c.name)

        # return '<%s *>'%self.__class__.__name__

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
