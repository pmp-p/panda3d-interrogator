# upy

FFI_MARK = '_C_'
RETURN_TYPE_FIRST = 1


import os
import sys
import ffi
import uctypes


class Engine:
    pass


CODE = {}

# fix micropython
import builtins

__dict__ = globals()


def vars(o=__import__("__main__")):
    try:
        return getattr(o, "__dict__")
    except:
        raise TypeError("vars() argument must have __dict__ attribute")


builtins.vars = vars

RET = 0
VAR = 1
FFI = 2


def dlopen(lib):
    code = {}

    # platform dependant
    clib = lib = f"lib{lib}_c.so"

    # FIXME: use readelf tools and wasm tools
    for func in os.popen(f"nm -C build/{lib} |grep '. T .*_*_.*$'|cut -d' ' -f3"):
        ffi_name = func.strip()
        if ffi_name.find(FFI_MARK) < 1:
            print("N/I: globals", func)
            continue

        try:
            if RETURN_TYPE_FIRST:
                func, ret, args = ffi_name.rsplit('_', 2)
            else:
                func, args, ret = ffi_name.rsplit('_', 2)
            cls, func = func.split('_C_', 1)
            code.setdefault(cls, {})
            code[cls].setdefault(func, [])
            code[cls][func].append((ret, args, ffi_name))

            print(cls, '.', func, args, '->', ret)
        except:
            print("N/I:", func)

    print("Loading native lib", lib, file=sys.stderr)

    try:
        lib = ffi.open(lib)
    except Exception as e:
        sys.print_exception(e)
        print(f'dlopen failed on {lib}')
        raise SystemExit
    code['lib'] = clib
    return code


def handle_return_type(indent, call, *args):
    opening = ""
    closing = ""
    rt = ""
    return f"""{' '*indent}return {rt}{opening}{call}{closing}"""


def is_tor(func):
    return func.startswith('ctor') or func.startswith('dtor')


def build(TARGET):
    global CODE

    OUT_FILE = open('build/%s.py' % TARGET, 'w')

    def write(*argv, **kw):
        print(*argv, **kw)
        kw['file'] = OUT_FILE
        print(*argv, **kw)

    def variadics(func, targets, ct='d'):
        write(f"    c.ct['{func}'] = {{")
        for t in targets:
            ret, args, ffi_name = t
            if ret == 'p' and args == 'v':
                write(f"""        {0} : ['s','{ret}', c.lib.func('{ret}','{ffi_name}','')],""")
            else:

                write(f"""        {len(t[VAR])} : ['{ct}','{ret}', c.lib.func('{ret}','{ffi_name}','{args}')],""")
        write('    }')

    CODE.update(dlopen(TARGET))

    lib = CODE.pop('lib')

    write(
        """# upy

import sys


if not '.' in sys.path: sys.path.insert(0,'.')
import interrogator.uplusplus as cxx

"""
    )

    for cls in CODE.keys():

        if not cls in ['Engine', 'NodePath', 'LVecBase3f']:
            print("SKIPPING", ":", cls)
            continue

        if cls.startswith('_'):
            pcls = cls[2:]
        else:
            pcls = cls

        write(
            f'''
class {pcls}(cxx.cplusplus):
    c = cxx.cstructs()
    c.name = """{pcls}@{lib[3:-3]}"""
    c.dlopen("""{lib}""")
'''
        )

        write(
            """
    # ctor/dtor
"""
        )

        for func, targets in CODE[cls].items():

            if not is_tor(func):
                continue

            if len(targets) == 1:
                for ret, args, ffi_name in targets:
                    write(f"""    c.ct['{func}'] = ['s','{ret}', c.lib.func('{ret}','{ffi_name}','{args}')]""")
            else:
                variadics(func, targets, 's')

        write(
            """
    # fixed pos
"""
        )

        for func, targets in CODE[cls].items():
            if is_tor(func) or (len(targets) != 1):
                continue

            for ret, args, ffi_name in targets:
                write(f"""    c.ct['{func}'] = ['d','{ret}', c.lib.func('{ret}','{ffi_name}','{args}')]""")

        write(
            """
    # variadic
"""
        )

        for func, targets in CODE[cls].items():
            if is_tor(func) or (len(targets) < 2):
                continue

            variadics(func, targets)

        write(
            """

    # c++ instance methods

    def __getattr__(self, attr):
        return self.__call(attr)

    del c.lib
"""
        )

    if TARGET == 'upanda3d':
        write(
            """
if __name__ == '__main__':
    import os
    import gc
    import time
    REFC = cxx.REFC
    GCBAD = cxx.GCBAD

    def test():
        print("C++ class constructor", Engine.c.ct['ctor'])
        E = Engine()
        print('engine      ',E)
        C = E.__class__( iptr=E )
        print('engine(copy)',C)

        # a dumb test that should say 42
        print('hello',E.HelloEngine())

        print('version','=', E.get_version_string())

        E.build()

        np = E.load_model( "model.bam" )

        print("np","=",np)

        E.attach(np)

        np = NodePath(cptr=np)

        v3 = LVecBase3f(0.01, 42.01, 0.01)
        print( v3, v3.get_x() , v3.get_y(), v3.get_z() )
        np.set_pos( v3 )

        v3 = LVecBase3f(2.0, 2.0, 2.0)
        print( v3, v3.get_x() , v3.get_y(), v3.get_z() )

        np.set_scale( v3 )




        while E.is_alive():
            E.step()

        print("C++ engine requested exit")
        del E
        print("deleting copy")
        del C

    print("--- test3 with refcounting ----")
    test()
    del test
    gc.collect()
    gc.collect()

    gc.collect()
    gc.collect()  # one more it's free !
    print(REFC)
    if GCBAD:print(" ----------- Bad GC ------------") # who said free ?

    #luckily we have 1 pointer left
    REFC = list(REFC.keys())
    while REFC:
        Engine( cptr = REFC.pop()).__del__()
"""
        )

    try:
        OUT_FILE.close()
    except:
        pass


if __name__ == '__main__':
    build('upanda3d')


#
