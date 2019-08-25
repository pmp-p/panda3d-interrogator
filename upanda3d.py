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

    for func in os.popen("nm -C {} |grep '. T .*_*_.$'|cut -d' ' -f3".format((lib))):
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


write = print


lib = CODE.pop('lib')

for cls in CODE.keys():
    write("class {}:".format((cls)))
    write()
    write('    lib = dlopen("""{})"""'.format((lib)))
    write()
    for func, targets in CODE[cls].items():
        for ret, args, ffi_name in targets:
            write('    {} = '.format((ffi_name)))
    write()
    for func, targets in CODE[cls].items():
        if not len(targets):
            continue

        write('    def {}(*argv,**kw):'.format((func)))

        if len(targets) == 1:
            ffi_name = targets[0][FFI]
            write('        return self.{}({})'.format((ffi_name), (targets[0][VAR])))
        else:
            for t in targets:
                ffi_name = t[FFI]
                if t[VAR] == 'v':
                    write('        if not len(argv): return self.{}()'.format((ffi_name)))
                else:
                    write('        if len(argv)=={}: self.{}({})'.format((len(t[VAR])), (ffi_name), (t[VAR])))
        write()


#
