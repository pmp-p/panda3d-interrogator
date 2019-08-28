print("uplusplus")

GCBAD = 0
REFC = {}


def djb2(s):
    hash = 5381
    for x in s:
        hash = ((hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF


import ffi


class cstructs(dict):
    def __init__(self):
        self.ct = dict()
        self.ref = dict()
        self.jit = dict()

    def dlopen(self, lib):
        self.lib = ffi.open(lib)


class cplusplus:
    def __cplusplus(self, call, *argv, **kw):

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
            try:
                if ftype == 'd':
                    return func(c.ref[id(self)], *argv)
                else:
                    return func(*argv)
            except KeyError:
                print(kw, ftype, rtype, func, "dangling ptr", id(self), c.ref)
                raise

        raise TypeError("%s : wrong count of positional arguments" % kw.get('hint', '?jit?'))

    def __call(self, attr):
        c = self.__class__.c
        if attr[0] != '_':
            hsum = '%s-%s' % (hash(attr), attr)  # should use djb2 to get cross interpreter
            jit = c.get(hsum, None)
            if jit is None:
                call = c.ct.get(attr, None)
                if call is not None:

                    def jit(*argv, **kw):
                        kw['hint'] = attr
                        return self.__cplusplus(call, *argv, **kw)

                    c[hsum] = jit
            return jit
        raise AttributeError("'{0}' C++ class has no method '{1}'".format(c.name, attr))

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
            c.ref[id(self)] = self.__cplusplus(c.ct['ctor'], *argv, **kw)

    def refcount(self):
        global REFC
        return REFC.get(self.__class__.c.ref[id(self)], 1)

    def __repr__(self):
        global REFC
        c = self.__class__.c
        return '<{0} *>({1}#{2})'.format(c.name, c.ref[id(self)], self.refcount())

    def __del__(self):
        global GCBAD
        c = self.__class__.c
        nref = self.refcount()
        if nref > 1:
            REFC[self.__iptr] -= 1
            print("still", nref - 1, "ref. on", c.ref[id(self)])
            return
        print("__del__", c.ref[id(self)])
        GCBAD -= 1
        try:
            self._['dtor'][2](c.ref[id(self)])
        finally:
            c.ref.pop(id(self))

    def __enter__(self, *argv, **kw):
        return self

    # self.__del__() is not called ...
    def __exit__(self, *argv, **kw):
        global REFC

        for attr in dir(self):
            try:
                if attr != '__del__':
                    delattr(self, attr)
            except:
                pass

        self.__del__()
