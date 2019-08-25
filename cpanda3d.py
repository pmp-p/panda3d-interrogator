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
    clib = lib = f"lib{lib}.so"

    for func in os.popen(f"nm -C {lib} |grep '. T .*_*_.$'|cut -d' ' -f3"):
        ffi_name = func.strip()
        if RETURN_TYPE_FIRST:
            func, ret, args = ffi_name.rsplit('_', 2)
        else:
            func, args, ret = ffi_name.rsplit('_', 2)
        try:
            cls, func = func.split('_C_', 1)
            code.setdefault(cls, {})
            code[cls].setdefault(func, [])
            code[cls][func].append((ret, args, ffi_name))

            print(cls, '.', func, args, '->', ret)
        except:
            print("N/I:", func)

    print("Loading native lib", lib, file=sys.stderr)
    lib = f"{LD_LIBRARY_PATH}/{lib}"
    try:
        lib = ffi.open(lib)
    except Exception as e:
        sys.print_exception(e)
        print(f'dlopen failed on {lib}')
        raise SystemExit
    code['lib'] = clib
    return code


CODE.update(dlopen('upanda3d_c'))


write = print


lib = CODE.pop('lib')

for cls in CODE.keys():
    write(f"class {cls}:")
    write()
    write(f'    lib = dlopen("""{lib})"""')
    write()
    for func, targets in CODE[cls].items():
        for ret, args, ffi_name in targets:
            write(f'    {ffi_name} = ')
    write()
    for func, targets in CODE[cls].items():
        if not len(targets):
            continue

        write(f'    def {func}(*argv,**kw):')

        if len(targets) == 1:
            ffi_name = targets[0][FFI]
            write(f'        return self.{ffi_name}({targets[0][VAR]})')
        else:
            for t in targets:
                ffi_name = t[FFI]
                if t[VAR] == 'v':
                    write(f'        if not len(argv): return self.{ffi_name}()')
                else:
                    write(f'        if len(argv)=={len(t[VAR])}: self.{ffi_name}({t[VAR]})')
        write()


#
