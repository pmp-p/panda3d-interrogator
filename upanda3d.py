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

class cplusplus:
    def variadic_call(self,ffi_name,*argv,**kw):
        func = getattr(self, ffi_name, {})
        try:
            if func:
                func = func.get(len(argv), None)

            if func:
                return func(self.iptr, *argv)
        except Exception as e:
            print(e,ffi_name,len(argv),func,'argv=',argv)
            raise
        raise TypeError("%s : wrong count of positional arguments" % ffi_name)

    # c++ ctor/dtor

    def __init__(self, *argv, **kw):
        self.iptr = self.ctor[len(argv)](*argv, **kw)

    def __del__(self):
        try:
            self.dtor(self.iptr)
        finally:
            self.iptr = None
"""
)


def handle_return_type(indent, call, *args):
    opening = ""
    closing = ""
    rt = ""
    return """{}return {}{}{}{}""".format((' '*indent), (rt), (opening), (call), (closing))


for cls in CODE.keys():

    if not cls in ['Engine', 'NodePath']:
        print("SKIPPING", ":", cls)
        continue

    if cls.startswith('_'):
        pcls = cls[1:]
    else:
        pcls = cls

    write("class {}(cplusplus):".format((pcls)))
    write()
    write('    lib = ffi.open("""{}""")'.format((lib)))
    write()

    for func, targets in CODE[cls].items():

        if len(targets) != 1:
            continue

        for ret, args, ffi_name in targets:
            write("""    {} = lib.func('{}','{}','{}')""".format((ffi_name), (ret), (ffi_name), (args)))

    write()
    write("# variadic")
    write()
    for func, targets in CODE[cls].items():
        if len(targets) < 2:
            continue

        write('    {} = {{'.format((func)))
        for t in targets:
            ret, args, ffi_name = t
            if ret == 'p' and args == 'v':  # ctor/dtor
                write("""        {} : lib.func('{}','{}',''),""".format((0), (ret), (ffi_name)))
            else:
                write("""        {} : lib.func('{}','{}','{}'),""".format((len(t[VAR])), (ret), (ffi_name), (args)))
        write('    }')

    write("\n# c++ instance methods\n")

    for func, targets in CODE[cls].items():
        #        if not len(targets):
        #            continue

        # keep constructor private
        if func == 'ctor':
            continue

        # FIXME static with multiples args may be not detected
        indent = 8

        if len(targets) == 1:
            ffi_name = targets[0][FFI]
            if ffi_name.endswith('_v'):
                write('    @classmethod'.format())
                write('    def {}(cls,*argv,**kw):'.format((func)))
                # write(f'        return cls.{ffi_name}(*argv, **kw)')
                write(handle_return_type(indent, 'cls.{}(*argv, **kw)'.format((ffi_name))))
            else:
                write('    def {}(self,*argv,**kw):'.format((func)))
                # write(f'        return self.{ffi_name}(self.iptr, *argv, **kw)')
                write(handle_return_type(indent, 'self.{}(self.iptr, *argv, **kw)'.format((ffi_name))))
        else:
            write('    def {}(*argv,**kw):'.format((func)))
            # write(f'        return variadic_call(self, {ffi_name}, *argv, **kw)')
            write(handle_return_type(indent, 'variadic_call(self, {}, *argv, **kw)'.format((ffi_name))))

        write()

write(
    """
print("C++ class constructor",Engine.ctor)
E = Engine()
print('engine',E)

# a dumb test that should say 42
print('hello',E.HelloEngine())

print('version','=', E.get_version_string())

E.build()

np = E.load_model( "model.bam" )

print("np","=",np)

E.attach(np)


while E.is_alive():
    E.step()

print("C++ engine requested exit")
E.__del__() # <== should not have to be called manually, cpython would do it itself.

"""
)


try:
    OUT_FILE.close()
except:
    pass
