# upy

FFI_MARK = '_C_'
RETURN_TYPE_FIRST = 1
LD_LIBRARY_PATH = "/data/cross/panda3d"


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
    clib = lib = "lib{}.so".format((lib))

    # FIXME: use readelf tools and wasm tools
    for func in os.popen("nm -C {} |grep '. T .*_*_.*$'|cut -d' ' -f3".format((lib))):
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
    lib = "{}/{}".format((LD_LIBRARY_PATH), (lib))
    try:
        lib = ffi.open(lib)
    except Exception as e:
        sys.print_exception(e)
        print('dlopen failed on {}'.format((lib)))
        raise SystemExit
    code['lib'] = clib
    return code


CODE.update(dlopen('upanda3d_c'))


def write(*argv, **kw):
    global OUT_FILE
    print(*argv, **kw)
    kw['file'] = OUT_FILE
    print(*argv, **kw)


# write = print


OUT_FILE = open('tests/testpy.py', 'w')


lib = CODE.pop('lib')


write(
    """# upy
import os
import sys
import ffi
import uctypes
import gc
import time


if not '.' in sys.path: sys.path.insert(0,'.')
from cplusplus import cplusplus, cstructs

"""
)


def handle_return_type(indent, call, *args):
    opening = ""
    closing = ""
    rt = ""
    return """{}return {}{}{}{}""".format((' '*indent), (rt), (opening), (call), (closing))


def variadics(func, targets, ct='d'):
    write("    c.ct['{}'] = {{".format((func)))
    for t in targets:
        ret, args, ffi_name = t
        if ret == 'p' and args == 'v':
            write("""        {} : ['s','{}', c.lib.func('{}','{}','')],""".format((0), (ret), (ret), (ffi_name)))
        else:

            write("""        {} : ['{}','{}', c.lib.func('{}','{}','{}')],""".format((len(t[VAR])), (ct), (ret), (ret), (ffi_name), (args)))
    write('    }')


def is_tor(func):
    return func.startswith('ctor') or func.startswith('dtor')


for cls in CODE.keys():

    if not cls in ['Engine', 'NodePath', 'LVecBase3f']:
        print("SKIPPING", ":", cls)
        continue

    if cls.startswith('_'):
        pcls = cls[2:]
    else:
        pcls = cls

    write(
        '''
class {}(cplusplus):
    c = cstructs()
    c.name = """{}@{}"""
    c.dlopen("""{}""")
'''
.format((pcls), (pcls), (lib[3:-3]), (lib))    )

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
                write("""    c.ct['{}'] = ['s','{}', c.lib.func('{}','{}','{}')]""".format((func), (ret), (ret), (ffi_name), (args)))
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
            write("""    c.ct['{}'] = ['d','{}', c.lib.func('{}','{}','{}')]""".format((func), (ret), (ret), (ffi_name), (args)))

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

"""
    )
    if 0:
        for func, targets in CODE[cls].items():

            # keep constructor private
            if func == 'ctor':
                continue

            # FIXME static with multiples args may be not detected
            indent = 8

            ffi_name = targets[0][FFI]

            if ffi_name.endswith('_v'):
                write('    @classmethod'.format())
                write('    def {}(cls, *argv, **kw):'.format((func)))
                write(handle_return_type(indent, 'cls.{}(*argv, **kw)'.format((ffi_name))))

            else:
                write('    def {}(self, *argv, **kw):'.format((func)))
                # ffi_name replace the argv slot of instance ptr so count is still good
                # write(f'        print("CALL=",getattr(self.__class__,"{ffi_name}"))')
                write(handle_return_type(indent, 'self.cplusplus("{}", *argv, **kw)'.format((ffi_name))))

            write()

    write(
        """
    del c.lib
"""
    )

#  (*param0).set_pos( const_cast<LVecBase3f*>(param1));
# lib/interrogate_wrapper.cpp:2763:53: error: no matching function for call to ‘NodePath::set_pos(LVecBase3f*)


write(
    """
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
    Engine.Engine_C_dtor_v_p(REFC.pop())

"""
)


try:
    OUT_FILE.close()
except:
    pass
