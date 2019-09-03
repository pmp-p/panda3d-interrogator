CLASS_SEPARATOR = "_C_"
RETURN_TYPE_FIRST = 1
DBG = 0


TARGET = 'build/interrogate'
TARGET_TMP = f'{TARGET}_temp.cpp'
TARGET_CPP = f'{TARGET}_wrapper.cpp'
TARGET_H = f'{TARGET}_wrapper.h'
TARGET_JSON = f'{TARGET}_wrapper.json'

FFI_MARK = '$'


import sys, os
import traceback
import argparse
import json


def print_exception(e, out, **kw):
    kw['file'] = out
    traceback.print_exc(**kw)


sys.print_exception = print_exception


# Parameters

parser = argparse.ArgumentParser()

parser.add_argument("--built", default='/usr/local', help="panda ./built directory or /usr /usr/local")
parser.add_argument("--source", default="./lib", help="cxx/h lib folder")
parser.add_argument("--name", default="", help="target lib name")
parser.add_argument("--toolchain", default="", help="toolchain root")
parser.add_argument("--sysroot", default="", help="toolchain sysroot")

args = parser.parse_args()


if os.path.exists(args.source):

    # os.chdir(inter.MODULE_PATH)
    inc = []
    if not args.built.startswith('/usr'):
        sys.path.insert(0, args.built)
        if not args.built in os.environ.get('LD_LIBRARY_PATH', ''):
            print(f"please prepend this : LD_LIBRARY_PATH={args.built}/lib ")
            raise SystemExit

    inc.append(f'{args.built}/include')
    inc.append(f'{args.built}/include/parser-inc')

    if not args.toolchain:
        inc.append('/usr/include')
        inc.append('/usr/include/x86_64-linux-gnu')

    # inc.append('/usr/lib/gcc/x86_64-linux-gnu/7/include')
    # inc.append('/usr/include/linux')
    # inc.append('/opt/sdk/wasi-sdk/share/wasi-sysroot/include')

    print(inc)

    relevant = 0
    try:
        import panda3d.core
    except ModuleNotFoundError:
        print(f"bad --built parameter, default is '{args.built}' but panda3d.core not found")
        raise SystemExit

    from . import interrogate as inter

    inter.PANDA_BUILD = args.built
    inter.MODULE_PATH = args.source
    inter.MODULE_NAME = args.name
    inter.VERBOSE_LVL = 1
    inter.BUILD_PATH = "./build"

    inter.interrogate(f"{inter.PANDA_BUILD}/bin/interrogate", "-promiscuous", "-string", "-fnames", "-assert", "-c", includes=inc)
    # ,"-fptrs")
else:
    print(f"--source folder invalid [args.source]")
    raise SystemExit


c_iptr = '?'
c_orig = ''
c_type1 = c_type2 = '?'
c_def = '?'
c_mn = '?'
c_va = ('void',)
c_code = []
c_block = 0
c_vars = []
var_args1 = ""
var_args2 = ""
relevant = 0
invalidate = 0


FFI_TYPE_MAP = {
    "": "v",
    "void": "v",
    "char const *": "s",
    "const char *": "s",
    "int": "i",
    "signed-char": "b",
    "unsigned-char": "B",
    "short": "h",
    "unsigned-short": "H",
    "int": "i",
    "unsigned-int": "I",
    "long": "l",
    "unsigned-long": "L",
    "long-long": "q",
    "unsigned-long-long": "Q",
    "enum": "i",
    "float": "f",
    "PN_stdfloat": "f",
    "double": "d",
    "uint8_t": "B",
    "uint16_t": "H",
    "uint32_t": "I",
    "ssize_t": "l",
    "_Bool": "B",
    "bool": "B",
}

FFI_MAP = {}
FFI_DECL = []


def stripped_list(l):
    return list(map(str.strip, l))


with open(TARGET_TMP, 'r') as C:

    basict = "void,char,short,unsigned,signed,int,long,float,double,long,byte,bool".split(',')
    basict.extend("std::size_t,wchar_t,std::streamsize,time_t".split(','))
    ptypes = []

    rtypes = {}

    from io import StringIO

    c_out = sys.stdout

    ##==========================================================================================================================
    def CPRINT(*code, **kw):
        kw['file'] = c_out
        # print(*code, **kw)

    ##==========================================================================================================================
    def make_ffi_names():
        global relevant, invalidate, c_orig, c_vars, c_def, c_iptr, c_type1, c_type2, c_mn, c_va, c_code, c_block, var_args1, var_args2

        if c_def[0] in '*&':
            qual = c_def[0]
            ffi = c_def[1:]
        else:
            qual = ''
            ffi = c_def

        # find ctor
        if ffi.find(FFI_MARK) > 0:
            cls, name = stripped_list(ffi.split(FFI_MARK))
            if cls == name:
                return qual, f"{cls}{FFI_MARK}ctor"
        # class method ?
        if ffi.startswith('static '):
            qual = 's'
        return qual, ffi

    ## =========================================================================================================================
    def map_return_types(bt, ffidef):
        if bt.find('<') > 0:
            bt = bt.split(' > ')[0].split('< ', 1)[-1]
            bt += ' *'

        bt = bt.split(' ', 1)[0]
        if bt.startswith('I_'):
            bt = bt[2:]

        if not bt in basict:
            cls, func = ffidef.split(FFI_MARK, 1)
            if cls.startswith('I_'):
                cls = cls[2:]

            ffidef = CLASS_SEPARATOR.join([cls, func])

            if bt in ptypes:
                rtypes[ffidef] = bt  # ptypes.index(bt)
            else:
                ptypes.append(bt)
                # rtypes[bt] = []

                # print(" RT :", bt, '%s->(...)' % cls)

    ##==========================================================================================================================
    def map_to_friendly():

        global FFI_DECL, c_vars, invalidate, var_args1, var_args2

        if invalidate:
            return

        qual, ffi = make_ffi_names()

        argi = ''
        disp = 0
        if ffi.count('NodePath_$_set_pos'):
            disp = 1
            print(ffi)
            print(c_orig)
            print("c_vars", c_vars)
            print("var_args1", var_args1)
            print("var_args2", var_args2)

        if c_vars[0] == '':
            start = 1  # static method
        else:
            start = 0

        # handle func(...,void)
        if c_vars[-1] == "void":
            end = -1
        else:
            end = 999

        args = c_vars[start:end]

        for a in args:
            # get only type, not C++ name but only if not void
            if a.count('*'):
                a = a.rsplit('*', 1)[0].strip() + ' *'
            elif a.count(' '):
                a = a.rsplit(' ', 1)[0].strip()

            if a.startswith('char const *'):
                argi += 's'
            elif '*' in a:
                argi += 'p'
            else:
                argi += FFI_TYPE_MAP.get(a.replace(' ', '').strip(), 'p')

        if not argi:
            argi = 'v'

        varsi = ', '.join(c_vars)

        # handle ctor case which is * _p_v() or * _p_%() for overloads and * func(void)
        if ffi.count(FFI_MARK + 'ctor'):
            reti = 'p'
            if argi == 'v':
                pass  # non overloaded default  * ctor(void)
            else:
                argi = argi[1:]  # overloaded

        else:
            # default is void _v_v(void)
            if c_orig.startswith('void '):
                reti = 'v'
            elif c_type1 not in ('void', ''):
                if c_type2 == 'char const *':
                    reti = 's'
                else:
                    reti = FFI_TYPE_MAP.get(c_type2, 'p')
            else:
                reti = 'p'

        # ffi = ffi.replace(FFI_MARK, f'__{ret}_?__')
        clash = 0
        if RETURN_TYPE_FIRST:
            test = ffi + f'_{reti}_{argi}'
            while test in FFI_DECL:
                clash += 1
                test = ffi + f'_{clash}_{reti}_{argi}'
        else:
            test = ffi + f'_{argi}_{reti}'
            while test in FFI_DECL:
                clash += 1
                test = ffi + f'_{clash}_{argi}_{reti}'

        ffi = test
        FFI_DECL.append(ffi)

        if ffi.count('get_wframe'):
            disp = 1

        # try to gather return type for complex types
        if reti == 'p':
            map_return_types(c_type2, ffi)

        FFI_MAP[c_mn] = {'ret': (reti, c_type2), 'args': (argi, varsi), 'qual': qual, 'ffi': ffi}

        if disp:
            print(c_mn, FFI_MAP[c_mn])

    ##==========================================================================================================================

    def process_line(cline):
        global relevant, invalidate, c_orig, c_vars, c_def, c_iptr, c_type1, c_type2, c_mn, c_va, c_code, c_block, var_args1, var_args2

        if cline.startswith('* '):  # original C++ def
            if cline.find('::operator') > 0:
                invalidate = 1
                if DBG:
                    print("SKIPPING", ":", c_orig)

            c_orig = cline[2:]
            c_def, var_args1 = c_orig.rsplit('(', 1)

            try:
                c_type1, c_def = c_def.strip().rsplit(' ', 1)
            except:
                c_type1 = ''
                c_def = c_def

            c_def = c_def.replace('::', FFI_MARK, 1)

            var_args1 = var_args1.split('(')[0]
            var_args1 = var_args1.rsplit(')', 1)[0]

            c_vars = stripped_list(var_args1.split(','))

        elif cline.startswith('_'):  # mangled name
            c_mn, var_args2 = cline.split('(', 1)
            var_args2 = var_args2.split('(')[0]
            var_args2 = var_args2.rsplit(')', 1)[0]

            CPRINT()

            if c_type1 != c_type2:
                CPRINT(f'//warning types [{c_type1}]!=[{c_type2}] ')

            if var_args1 != var_args2:
                CPRINT(f'//warning args [{var_args1}]!=[{var_args2}] ')

            v = stripped_list(var_args2.split(','))
            c_iptr = v[0]

            v = stripped_list(var_args1.split(','))
            v.insert(0, c_iptr)

            var_args1 = ', '.join(v)

            v[0] = 'self->instance_ptr'
            var_args2 = ', '.join(v)

            code = '\n'.join(c_code)

            # add self since C++ don't mention "this" in (...)
            c_vars.insert(0, c_iptr)

            map_to_friendly()

            CPRINT(
                f"""
#ifndef MODGEN

EXPORT_FUNC mp_obj_t
{c_def}({var_args1}) {{
{code}
}}

#else

def {c_def}({var_args1}) -> {c_type1 or 'void'}:
    mp_obj_t result;
    // {c_mn}({var_args2});

{code}

#endif // {c_orig}


""".replace(
                    FFI_MARK, CLASS_SEPARATOR
                )
            )
            c_block = 1
            relevant = 0
            c_type1 = c_type2 = '?'
            c_def = '?'
            c_mn = '?'
            var_args1 = var_args2 = ('void',)
            c_code = []
            c_vars = []

        else:  # type
            c_type2 = cline

    for cline in C.readlines():
        # ==== skip
        if cline.startswith(' * C wrapper for'):
            relevant = 1
            invalidate = 0
            continue

        if cline.endswith('*/') or cline.startswith('/*'):
            # print('SKIP:', cline)
            continue

        # =========
        if invalidate:
            if DBG:
                print(cline, end='')

        if relevant:
            cline = cline.strip()

            try:
                process_line(cline)
            except Exception as e:
                sys.print_exception(e, sys.stderr)
                print(f" ---------> {cline} <--------------")
                raise SystemExit

        elif c_block:
            cline = cline.strip()

            if cline.endswith('}'):
                c_block = 0
                relevant = 0
                invalidate = 0
            else:
                c_code.append(f'    {cline}')


with open(TARGET_TMP, 'r') as C, open(TARGET_CPP, 'w') as CPP:
    for l in C.readlines():
        for k, v in FFI_MAP.items():
            l = l.replace(k, v['ffi'])
        l = l.replace(FFI_MARK, CLASS_SEPARATOR)
        l = l.replace('static string ', 'static std::string ')
        l = l.replace('static wstring ', 'static std::wstring ')
        l = l.replace('I_NodePath', 'NodePath')
        CPP.write(l)


# =================================================================

# fmt: off
h_map = {
    'std::size_t '  : 'unsigned int ',
    'std::streamsize' : 'int ',
    'PN_stdfloat '  : 'float ',
    'wchar_t const ': 'char const ',
    'PointerTo< WindowFramework > ': 'char ',
#    'time_t ' : None,
}

# fmt: on


ptypes.sort()
ptypes.reverse()


print("PTYPES:", ptypes)

# for k, v in rtypes.items():
#    print(v, k)


with open(TARGET_JSON, 'w') as RT:
    print(json.dumps({'forward_decl': ptypes, 'retmap': rtypes}), file=RT)

# =================================================================


with open(TARGET_CPP, 'r') as C, open(TARGET_H, 'w') as H:

    def CARG(cpp):
        global h_map
        for k, v in h_map.items():
            if v is None:
                if l.find(k) >= 0:
                    askip = 1
                    break
            else:
                cpp = cpp.replace(k, v)
        else:
            askip = 0
        return cpp, askip

    H.write(
        """
#include <stdio.h>
#include <stdbool.h>
#include <time.h>

#define PT char
#define string char const
#define PN_stdfloat float


"""
    )

    for pt in ptypes:
        # H.write(f"#define {pt.replace('::','$$')} char\n")
        H.write(f"#define {pt.replace('::','__')} char\n")

    H.write("\n")
    cut = 'EXPORT_FUNC '
    lcut = len(cut)

    for l in C.readlines():
        if not l.startswith(cut):
            continue
        skip = 0

        decl, params = l[lcut:].strip()[:-2].split('(', 1)

        c_args = []

        if len(params):
            for idx, cpp in enumerate(params.split(', ')):
                if idx == 0:
                    baset = cpp.split(' ', 1)[0].strip()
                    baset += CLASS_SEPARATOR
                    if decl.count(baset):
                        c_args.append(cpp)
                        continue

                    # print("c.h warning (", baset, ') from :', decl)
                    c_args.append(f'char *param{idx}')

                elif '::' in cpp:
                    c_args.append(f'char *param{idx}')
                elif '*' in cpp:
                    c_args.append(f'char *param{idx}')
                else:
                    c_args.append(CARG(cpp)[0])

        decl, skip = CARG(decl)

        if decl.find('::') > 0:
            rt, decl = decl.split(' ', 1)
            # decl = f"{rt.replace('::','$$')} {decl}"
            decl = f"{rt.replace('::','__')} {decl}"

        if decl.find('PointerTo<') >= 0:
            skip = 1

        if not skip:
            H.write(f"extern {decl}({', '.join(c_args)});\n")
        else:
            print("c.h unsupported C++ return type :", decl)


#
