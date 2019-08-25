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

def variadic_call(self,ffi_name,*argv,**kw):
    func = cls.get(ffi_name,{})

    if func:
        func = func.get( len(argv) , None)

    if func:
        return func(self.iptr, *argv)

    raise TypeError("%s : wrong count of positional arguments" % ffi_name)

"""
)


for cls in CODE.keys():

    if not cls in ['Engine', 'PandaSystem']:
        print("SKIPPING", ":", cls)
        continue

    write(f"class {cls}:")
    write()
    write(f'    lib = ffi.open("""{lib}""")')
    write()

    for func, targets in CODE[cls].items():

        if len(targets) != 1:
            continue

        for ret, args, ffi_name in targets:
            write(f"""    {ffi_name} = lib.func('{ret}','{ffi_name}','{args}')""")

    write()
    write("# variadic")
    write()
    for func, targets in CODE[cls].items():
        if not len(targets):
            continue

        if len(targets) < 2:
            continue

        write(f'    {func} = {{')
        for t in targets:
            ret, args, ffi_name = t
            if ret == 'p' and args == 'v':  # ctor
                write(f"""        {0} : lib.func('{ret}','{ffi_name}',''),""")
            else:
                write(f"""        {len(t[VAR])} : lib.func('{ret}','{ffi_name}','{args}'),""")
        write('    }')

    write("# c++ ctor\n")

    write(f"    def __init__(self, *argv, **kw):")
    write(f"        self.iptr = variadic_call(self, 'ctor', *argv, **kw)")

    write("\n# c++ instance methods\n")

    for func, targets in CODE[cls].items():
        if not len(targets):
            continue

        # FIXME static with multiples args may be not detected

        if len(targets) == 1:
            ffi_name = targets[0][FFI]
            if ffi_name.endswith('_v'):
                write(f'    @classmethod')
                write(f'    def {func}(cls,*argv,**kw):')
                write(f'        return cls.{ffi_name}(*argv, **kw)')
            else:
                write(f'    def {func}(self,*argv,**kw):')
                write(f'        return self.{ffi_name}(self.iptr, *argv, **kw)')
        else:
            write(f'    def {func}(*argv,**kw):')
            write(f'        return variadic_call(self, {ffi_name}, *argv, **kw)')

        write()


try:
    OUT_FILE.close()
except:
    pass
