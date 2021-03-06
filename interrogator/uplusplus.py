# uplusplus
try:
    const(0)
except:
    def const(x):return x

TRACE = 0
GCBAD = 0
REFC = {}
REFCOUNTED = None
INCREF = None
DECREF = None


FFI_TRACK = {}


#def djb2(s):
#    hash = 5381
#    for x in s:
#        hash = ((hash << 5) + hash) + ord(x)
#    return hash & 0xFFFFFFFF


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
IDX_SIG = const(4)


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


#def wrap(call, rt, argv, kw, instance=None):
#    if TRACE:
#        print("  wrap", 'instance=', instance, argv, kw)
#
#    if instance is None:
#        argv, kw = cxx_stack(*argv, **kw)
#        jt = '  JIT-s'
#    else:
#        argv, kw = cxx_stack(instance, *argv, **kw)
#        jt = '  JIT-d'
#
#    rv = call(*argv)
#    print(jt, 'CPTR rv=', rv)
#    rv = rt(cptr=rv)
#    print(jt, 'PTYPE(%s) rv=' % rt, rv)
#    return rv



# basic return types could be optimized saving the passthrough call

# empty call stack could be optimized via direct function pointer call

# kw could be used to pass runtime jit info


def call1(ancestor, cls, instance, attr, decl):
    c = cls.c

    ct = decl[IDX_CT]
    rt = decl[IDX_RET]

    argc = decl[IDX_ARGC]

    if isinstance(rt, int) and (attr != 'ctor'):
        if TRACE:
            print("   JIT-1", rt, c.decl[rt])
        rt = c.decl[rt]
    else:
        if TRACE:
            print("   JIT-1 passthrough")
        rt = passthrough

    # OPTIM
    # for TRACE
    ffi = c.get('%s-ffi' % attr, None)
    if ffi is None:
        ffi = ancestor.c.lib.func(*decl[IDX_FFI])
        c['%s-ffi' % attr] = ffi



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
                print("   JIT-1-(this, *", argv, ')')
            argv, kw = cxx_stack(instance, *argv, **kw)
            if TRACE:
                print("   JIT-1", argv, FFI_TRACK[id(ffi)])
            return rt(cptr=ffi(*argv))

    FFI_TRACK[id(ffi)] = decl
    ancestor.c[attr] = jit1

    # alias to parent so child can call directly next time
    #if (ancestor is not cls):
    c[attr] = jit1

    # no polymorphim

    # if instance and (ancestor is not cls):
    # if instance:
    #   instance.c[attr]=jit1

    return jit1





def get_match(ancestor, cls, rt, ct, pl, argc):
    cando = []
    for proto in pl:
        if ct != proto[IDX_CT]:
            if TRACE:
                print("   calltype!=%s for" % ct, proto)
            continue

        if argc < proto[IDX_ARGC]:
            if TRACE:
                print("   argc<%d for" % argc, proto)
            break

        elif argc == proto[IDX_ARGC]:
            if TRACE:
                print("   argc==%d for" % argc, proto)
            cando.append(proto)
    return cando


def get_ffi_call_sig(argv):
    sig = []
    for a in argv:
        if isinstance(a, str):
            sig.append('s')
        elif isinstance(a, float):
            sig.append('f')
        else:
            # assume int is maybe pointer
            sig.append('?')
    return ''.join(sig)


# can give false positive, but no false negative
def fuzzy_check(sig, match):
    for idx, c in enumerate(sig):
        if (c == '?') and (match[idx] == 'p'):
            continue
        if c != match[idx]:
            return False
    return True

def fuzzy2(offer,canhave):
    print(f"{offer=}{canhave=}")


def callx(ancestor, cls, instance, rt, ct, pl, attr, argc, argv, kw):
    global TRACE
    #
    sigkey = '{}-{}'.format(attr, argc)
    #

    if TRACE:
        print('  JIT-x CACHING', sigkey, argc)

    cl = []
    for proto in get_match(ancestor, cls, rt, ct, pl, argc):
        ffi = ancestor.c.lib.func(*proto[IDX_FFI])
        FFI_TRACK[id(ffi)] = proto[IDX_FFI]
        cl.append([ffi, proto[IDX_SIG]])

    if not len(cl):
        for p in pl:
            print(p)  # [IDX_FFI])
        raise TypeError("%s->%s : no match for arguments count %d" % (ancestor.__name__, attr, argc))

    # FIXME: that block would need *HUGE* optim and should take shortcuts.

    if len(cl) > 1:
        # must forbid caching until someday maybe code paths can be learned ( access to line+module of caller ? )

        sigkey = get_ffi_call_sig(argv)
        cando = []

        for proto in get_match(ancestor, cls, rt, ct, pl, argc):
            if repr(proto[IDX_SIG]).find('&&')>0:
                if TRACE:
                    print("REJ (moving) [%s]" % sigkey, proto[IDX_FFI][2], proto[IDX_SIG])
                continue
            if fuzzy_check(sigkey, proto[IDX_FFI][2]):
                if TRACE:
                    print("[%s]" % sigkey, proto[IDX_FFI][2], proto[IDX_SIG])
                cando.append(proto)
            else:

                if TRACE:
                    print("REJ (mismatch) [%s]" % sigkey, proto[IDX_FFI][2], proto[IDX_SIG])

        print(f"236: #FIXME: use isinstance {cl=}")

        #TRACE=1
        cl = []


        for proto in cando:
            for argpos,arg in enumerate(argv):
                if not isinstance(arg, cplusplus):
                    continue
                #if isinstance(arg, theprotoclass):
                if proto[IDX_SIG][argpos].find(arg.__class__.__name__)>=0:
                    if TRACE:
                        print("*SELECTEd* [%s]" % sigkey, proto[IDX_FFI][2], proto[IDX_SIG])
                    ffi = ancestor.c.lib.func(*proto[IDX_FFI])
                    FFI_TRACK[id(ffi)] = proto[IDX_FFI]
                    cl.append([ffi, proto[IDX_SIG]])

                # fuzzy2 FIXME: this is horrible
                elif proto[IDX_SIG][argpos].split(' ',1)[0] in arg.__class__.__name__:
                    ffi = ancestor.c.lib.func(*proto[IDX_FFI])
                    FFI_TRACK[id(ffi)] = proto[IDX_FFI]
                    cl.append([ffi, proto[IDX_SIG]])

                elif TRACE:
                    print("REJ (FIXME: class hierarchy) [%s]" % sigkey, proto[IDX_FFI][2], proto[IDX_SIG])
                    print(f"{arg=} {proto[IDX_SIG]=}")

        if not len(cl):
            for proto in get_match(ancestor, cls, rt, ct, pl, argc):
                for argpos,arg in enumerate(argv):
                    fuzzy2(arg.__class__.__name__,proto[IDX_SIG])

        if len(cl)>1:
            print("\n  JIT-x ERROR N/I call sig dependant proto")
            print("  ========================================")
            print()

        # forbid caching
        sigkey = None


    cl = cl[-1][0]

    if instance:

        def jit_n(*argv, **kw):
            if TRACE:
                print("   JIT[%d]-d%s" % (argc, ct), argv, FFI_TRACK[id(cl)])

            argv, kw = cxx_stack(instance, *argv, **kw)
            return rt(cptr=cl(*argv))

    else:

        def jit_n(*argv, **kw):
            if TRACE:
                print("   JIT[%d]-s%s" % (argc, ct), argv, FFI_TRACK[id(cl)])

            argv, kw = cxx_stack(*argv, **kw)
            return rt(cptr=cl(*argv))

    # cache if allowed
    if sigkey:
        ancestor.c[sigkey] = jit_n

        # alias to parent so child can call directly next time
        cls.c[sigkey] = jit_n

    return jit_n(*argv, **kw)


def jit_table(cls, instance, attr):
    global TRACE

    mro = [instance]

    if instance is None:
        mro.append(cls)

    mro.extend(cls.__bases__)

    for c in cls.__bases__:
        for b in c.__bases__:  # TODO: recurse more ?
            if not b in mro:
                mro.append(b)

    if DBG:
        print("inspecting", mro)

    # maybe self maybe not
    for call_ancestor, ancestor in enumerate(mro):

        # static call has [none, ] in mro first slot so skip it
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
                    return cl(*argv, **kw)
                if TRACE:
                    print("JITx s[%s-%d] %s->%s(*%s, **%s) -> %s" % (ct, argc, ancestor, attr, argv, kw, rt))
                return callx(ancestor, cls, instance, rt, ct, pl, attr, argc, argv, kw)

        else:

            def jit_x(*argv, **kw):
                argc = len(argv) + len(kw)  # +1
                sigkey = '{}-{}'.format(attr, argc)
                cl = instance.c.get(sigkey, None)
                if cl:
                    return cl(*argv, **kw)
                if TRACE:
                    print("JITx d[%s-%d] %s->%s(%s, * %s, **%s) -> %s" % (ct, argc, ancestor, attr, instance, argv, kw, rt))
                return callx(ancestor, cls, instance, rt, ct, pl, attr, argc, argv, kw)

        return jit_x

    raise Exception("MRO%s->%s not found" % (mro, attr))


class cstructs(dict):

    lib = None

    pool = []
    ipool = []
    nursery = []

    # autoload ?
    i = None

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

        # how to get cross interpreter to match instances ?
        hsum = '%s-%s' % (id(self), attr)

        jit = self.get(hsum, None)
        # OPTIM
        if jit is None or TRACE:
            try:
                jit = jit_table(cls, instance, attr)
            except Exception as e:
                sys.print_exception(e, sys.stdout)
                raise Exception("%s->%s jit compilation failed" % (c.name, attr))
            c[hsum] = jit
        return jit

        if instance:
            raise AttributeError("'{0}' C++ class has no method '{1}'".format(c.name, attr))
        raise AttributeError("'{0}->{1}' is not a C++ static".format(c.name, attr))

    def destroy(self, instance):
        print('448:',instance)


class cplusplus:

    # c++ ctor/dtor

    # ffi call interface 2 types of calls   f(this, ...)  f( ... )

    def __init__(self, *argv, **kw):
        global GCBAD, REFC
        c = self.__class__.c
        iref = kw.pop('iptr', None)
        cref = kw.pop('cptr', None)

        if iref or cref:
            if TRACE:
                print("    __RETREF__( %s iref=%s cref=%s)" % (c.name, iref, cref))

            # extract pointer addr from source
            if (cref is not None) and (not isinstance(cref, int)):
                print("ERROR cref is not a raw pointer but a ", cref)
                iref = cref

            if isinstance(iref, cplusplus):
                if iref.__class__ is not self.__class__:
                    print("cannot do link %s on different type %s" % (iref.__class__, self.__class__))
                cref = c.ref[id(iref)]

            # add the cref to class handler for this instance
            c.ref[id(self)] = cref
            r = REFC.setdefault(cref, 1)
            REFC[cref] += 1
            # do ->ref() on C++ side on first use
            if (r == 1) and REFCOUNTED and isinstance(self, REFCOUNTED):
                if 1:  # TRACE:
                    print("   REF %s" % INCREF(cref), 'on', self)
                else:
                    INCREF(cref)
            return

        if TRACE:
            print("    __init__( %s iref=%s cref=%s)" % (c.name, iref, cref))

        GCBAD += 1
        # should be a passthrough that return only C pointer
        if TRACE:
            ctor = jit_table(self.__class__, None, 'ctor')
            cref = ctor(*argv, **kw)
            if not isinstance(cref, int):
                print("455 : ERROR __init__ ->", cref, " : expected a raw pointer")
            c.ref[id(self)] = cref
            return
        c.ref[id(self)] = jit_table(self.__class__, None, 'ctor')(*argv, **kw)

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
            # c.ct.get('dtor', ['', '', noop])[2](item)

    # luckily we have the pointers left in cstructs of each classes


#
