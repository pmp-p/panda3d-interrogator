# upy

# Experimental JavaScript interpreter for FreeBSD (Duktape FFI Experimentation)
# https://github.com/davidchisnall/jsrun


# py: __del__ special method not implemented for user-defined classes
# BLOCKER: https://github.com/micropython/micropython/issues/1878

# PEP572 https://github.com/micropython/micropython/pull/4908

# next()
# https://github.com/micropython/micropython/issues/5046


# STM GC
#   https://bitbucket.org/pypy/stmgc/src/default/

# ffi
#   https://pycopy.readthedocs.io/en/latest/library/ffi.html

# jni
#   https://github.com/pfalcon/pycopy/blob/pfalcon/ports/unix/modjni.c

# llvm
#   https://github.com/pfalcon/ullvm


# https://github.com/pfalcon/awesome-micropython


# raspi3 fib(34) => 34s    PC+2: 36s


# Py

# PyPy, IronPython, Jython, MicroPython, StacklessPython, WPython, Pyston,
# Hotpy, Unladen Swallow, Pyjion, pythran, Python2C, Brython, Batavia, VOC
# https://github.com/naftaliharris/tauthon
# https://github.com/go-python/gpython

# Optimizers/compilers : Cython, Nuitka
# https://github.com/grumpyhome/grumpy


FFI_MARK = '_C_'
CNI = 0

RETURN_TYPE_FIRST = 1

DBG = 0


import sys

import upy as os

import upy.ffilib as ffilib


try:
    import uctypes
except:
    print('CPY')

try:
    import ffi
except:
    print("FIXME: cpython")


try:
    import ujson as json
except:
    import json


CODE = {}


RT_UNSOLVED = []


# fix micropython
import builtins

__dict__ = globals()


def vars(o=__import__("__main__")):
    try:
        return getattr(o, "__dict__")
    except:
        raise TypeError("vars() argument must have __dict__ attribute")


builtins.vars = vars

CTP = 0
RET = 1
VAR = 2
FFI = 3


def dlopen(lib):

    with open(f"build/{lib}.json", 'r') as jsonf:
        code = json.loads(jsonf.read())

    # platform dependant
    if CNI:
        clib = f"lib{lib}_cni.so"
    else:
        clib = f"lib{lib}_c.so"

    def ffimap(ffi_name):
        global RETURN_TYPE_FIRST
        if RETURN_TYPE_FIRST:
            func, ret, args = ffi_name.rsplit('_', 2)
        else:
            func, args, ret = ffi_name.rsplit('_', 2)
        return func, ret, args

    # FIXME: use readelf tools and wasm tools
    # for func in os.popen(f"nm --demangle --defined-only --dynamic {clib} |grep '. T .*_._.*$'|cut -d' ' -f3"):
    for func in os.popen(f"nm -C build/{clib} |grep '. T .*_*_.*$'|cut -d' ' -f3"):
        ffi_name = func.strip()
        if ffi_name.find(FFI_MARK) < 1:
            if DBG:
                print("N/I: globals", func, end='')
            continue

        try:
            func, ret, args = ffimap(ffi_name)
            cls, func = func.split(FFI_MARK, 1)
            code.setdefault(cls, {})
            code[cls].setdefault(func, [])
            code[cls][func].append((code['callmap'].get(ffi_name, 'd'), ret, args, ffi_name))

            if DBG:
                print(cls, '.', func, args, '->', ret)
        except:
            if DBG:
                print("N/I:", func, end='')

    print("Loading native lib", clib, file=sys.stderr)

    try:
        lib = ffi.open(clib)
    except Exception as e:
        sys.print_exception(e)
        print(f'dlopen failed on {clib}')
        raise SystemExit

    code['lib'] = clib
    del code['btypes']

    forward_decl = []
    cls = code['classes']
    ck = list(cls.keys())
    ck.sort()
    mx = 0
    for cn in ck:
        mx = max(mx, len(cls[cn]['bases']))

    print('MAX PARENTS =', mx)
    for p in range(mx + 1):
        lot = []
        for cn in ck:
            if p == len(cls[cn]['bases']):
                lot.append(cn)

        lot.sort()
        forward_decl.extend(lot)

    print(forward_decl)
    forward_decl = sort_inheritance(code, forward_decl)
    forward_decl = sort_inheritance(code, forward_decl)
    code['forward_decl'] = sort_inheritance(code, forward_decl)

    return code


# sort all the classes in order to use python class hierarchy and isinstance can work normally


def sort_inheritance(code, fwd):
    def bases(cn):
        return list(cls[cn]['bases'])

    # fwd = code['forward_decl']

    cls = code['classes']

    ancestor = ''
    initial = 0

    for cn in fwd:
        if len(bases(cn)):
            break
        initial += 1

    first = initial

    while True:
        changes = 0

        child = fwd[first]
        parents = bases(fwd[first])

        for i in range(first):
            ancestor = fwd[i]
            if ancestor in parents:
                parents.remove(ancestor)

        if len(parents):
            print(child, 'is before', parents)

            ancestor = parents.pop(0)

            try:
                child_place = fwd.index(ancestor)
            except:
                print("\n\n", ancestor, 'not found, please forcetype and rebuild\n\n')
                for e in fwd:
                    print('  ', e)
                raise SystemExit

            fwd.remove(child)
            fwd.insert(child_place, child)
            changes += 1

        if not changes:
            first += 1
            if first == len(fwd):
                break
        else:
            first = initial
    return fwd


def handle_return_type(indent, call, *args):
    opening = ""
    closing = ""
    rt = ""
    return f"""{' '*indent}return {rt}{opening}{call}{closing}"""


def is_tor(func):
    return func.startswith('ctor') or func.startswith('dtor')


def build(TARGET):
    global CODE, DBG

    OUT_FILE = open('build/%s.py' % TARGET, 'w')

    def write(*argv, **kw):
        global DBG
        if DBG:
            print(*argv, **kw)
        kw['file'] = OUT_FILE
        print(*argv, **kw)

    def ret_cpp(ret, ffi_name, hint=''):
        global RT_UNSOLVED
        pret = "'%s'" % ret
        if ret == 'p':
            if ffi_name in forward_decl:
                pret = forward_decl.index(ffi_name)
            elif not ffi_name in RT_UNSOLVED:
                RT_UNSOLVED.append([ffi_name, hint])

        return pret, ffi_name

    def enums(cls, no_const, indent=0):
        for enum_name, enums in cls['enums'].items():
            write(
                f"""{"    "*indent}# enum {enum_name}
"""
            )

            for enum in enums:
                if enum[0] in no_const:
                    write(f"""{"    "*indent}{enum[0]} = {enum[1]}""")
                else:
                    write(f"""{"    "*indent}{enum[0]} = const({enum[1]})""")

            write("\n")

    CODE.update(dlopen(TARGET))

    lib = CODE['lib']

    forward_decl = CODE['forward_decl']

    has_main_enum = forward_decl[0] == ''

    if has_main_enum:
        forward_decl.pop(0)

    write(
        f"""# upy

import sys

try:
    const(0)
except:
    def const(x):return x
    import ctypes
    sys.modules['uctypes']=ctypes

if not '.' in sys.path: sys.path.insert(0,'.')
import interrogator.uplusplus as cxx

extern = cxx.cstructs.decl.append"""
    )

    classes = CODE['classes']

    for cn in forward_decl:
        write(f"extern('{cn}') # {', '.join(classes[cn]['bases'])}")

    write("del extern\n")

    if has_main_enum:
        enums(classes[''], CODE['no_const'], indent=0)

    indent = 1

    for cn in forward_decl:
        ancestor = 'cxx.cplusplus'
        if len(classes[cn]['bases']):
            ancestor = ', '.join(classes[cn]['bases'])

        write(
            f'''
class {cn}({ancestor}):
    __bases__ = tuple([{', '.join(classes[cn]['bases'])}])
    c = cxx.cstructs()
    c.register("{cn}", "{TARGET}", """{lib}""")
'''
        )
        enums(classes[cn], CODE['no_const'], indent=1)
        # write("# ============== ENUM OFF ====================")

        def dump(cls, ct, ctor=0):
            global CNI

            fnlist = []

            for proto in cls['proto']:
                if proto['ctor'] != ctor:
                    continue

                if proto['ct'] != ct:
                    continue

                if not proto['fn'] in fnlist:
                    fnlist.append(proto['fn'])
            fnlist.sort()

            for func in fnlist:
                if ctor:
                    write(f"{'    '*indent}c.ct['ctor'] = [")
                else:
                    write(f"{'    '*indent}c.ct['{func}'] = [")

                for proto in cls['proto']:
                    if proto['fn'] != func:
                        continue

                    ret = proto['cni_rt']
                    pret, cret = ret_cpp(ret, proto['rt'], "%s : %s : %s" % (proto['cni_rt'], proto['c_rt'], proto['cpp_ref']))

                    args = proto['cni_args']
                    if CNI:
                        ffi_name = proto['cni']
                    else:
                        ffi_name = proto['indexed']

                    cffi = f"('{ret}', '{ffi_name}', '{args}')"

                    # kw arguments ?
                    write(f"{'    '*indent}    ('{ct}', {pret}, {proto['argc']}, {cffi}, {proto['argt']}),")

                write(f"{'    '*indent}]")

            write("")
            return fnlist

        write("    # ctor/dtor\n")

        dump(classes[cn], 's', ctor=1)

        write("    # classmethod type calls\n")

        for cm in dump(classes[cn], 's', ctor=0):
            write(
                f"""{'    '*indent}@classmethod
{'    '*indent}def {cm}(cls, *args,**kw):
{'    '*indent}    return ( cls.c.get('{cm}', None) or cls.c.call({cn}, '{cm}', None) )(*args,**kw)
"""
            )

        write("    # instance method type calls\n")

        dump(classes[cn], 'd', ctor=0)

        write(
            f"""
{'    '*indent}# c++ instance methods

{'    '*indent}def __del__(self):
{'    '*indent}    self.c.destroy(self)

{'    '*indent}def __getattr__(self, attr):
{'    '*indent}    return self.c.get(attr,None) or  self.c.call({cn}, attr, self)

{cn}.c.link({cn})

"""
        )
    write(
        """

cxx.REFCOUNTED = ReferenceCount
cxx.INCREF = Engine.inc_ref
cxx.DECREF = Engine.dec_ref
"""
    )

    if 1:
        RT_UNSOLVED.sort()
        for rt in RT_UNSOLVED:
            print("407: WARNING unresolved forward types :", rt)
    else:
        print("410: WARNING unresolved forward types listing disabled")

    if TARGET == 'upanda3d':
        write(
            """



if __name__ == '__main__':
    import os
    import gc
    import time
    import uctypes
    REFC = cxx.REFC

    def test():


        for proto in Engine.c.ct['ctor']:
            print("C++ class constructor", proto)

        E = Engine()

        print('engine      ',E)
        C = E.__class__( iptr=E )
        print('engine(copy)',C)

        # a dumb test that should say 42
        print('hello',E.HelloEngine())

        print('version','=', E.get_version_string())

        E.build()

        pf = E.get_framework()
        print('PandaFramework=', pf )

        wf = E.get_wframe()

        print('WindowFramework=', wf )


        np = E.load_model( "boris.bam" )

        print("np","=",np)

        E.attach(np)


        Vec3 = LVecBase3f


        v3 = Vec3(0.01, 42.01, 0.01)
        print("Vec3=", v3)


        np.set_pos( v3 )

        v3 = Vec3(2.0, 2.0, 2.0)
        print( v3, v3.get_x() , v3.get_y(), v3.get_z() )

        np.set_scale( v3 )

        np.set_pos( Vec3(.0,42.,0.) )


        #cube = E.new_Cube(1.0, "CubeMaker", "Data")
        #print('cube=',cube)

        while E.is_alive():
            E.step()
            gc.collect()
            time.sleep(.016)

        print("C++ engine requested exit")
        del E
        print("deleting copy")
        del C

    #print("--- test3 with refcounting ----")
    #test()

    if len(sys.argv) and sys.argv[-1].endswith('.py'):
        code = compile( open( sys.argv[-1], 'r').read(), sys.argv[-1] , 'exec' )
        exec( code, globals() , globals() )




    del test
    gc.collect()
    gc.collect()

    cxx.gc()

"""
        )

    try:
        OUT_FILE.close()
    except:
        pass


if __name__ == '__main__':
    build('upanda3d')


#
