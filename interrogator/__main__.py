CLASS_SEPARATOR = "_C_"
RETURN_TYPE_FIRST = 1
DBG = 0

FFI_MARK = '_$_'
import sys, os
import traceback


def print_exception(e, out, **kw):
    kw['file'] = out
    traceback.print_exc(**kw)


sys.print_exception = print_exception


from . import interrogate as inter

# Parameters
inter.MODULE_PATH = sys.argv[1]
inter.MODULE_NAME = sys.argv[1].rsplit('/')[-1]

inter.VERBOSE_LVL = int(sys.argv[2])  # Assume the user did specify something valid


if len(sys.argv) != 3:
    debug_out("Usage: python interrogate.py <module-name> <verbose-level>")
    sys.exit(1)


TARGET_TMP = 'interrogate_temp.cpp'
TARGET_CPP = 'interrogate_wrapper.cpp'


# Change into the source directory
if os.path.exists(inter.MODULE_PATH):
    os.chdir(inter.MODULE_PATH)

    inter.interrogate("interrogate", "-promiscuous", "-string", "-c", "-fnames")  # ,"-fptrs")

    relevant = 0


else:
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

    ##==========================================================================================================================
    def map_to_friendly():

        global FFI_DECL, c_vars, invalidate, var_args1, var_args2

        if invalidate:
            return

        qual, ffi = make_ffi_names()

        argi = ''
        disp = 0
        if ffi.count('Engine_$_get_version_string'):
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
        FFI_MAP[c_mn] = {'ret': (reti, c_type2), 'args': (argi, varsi), 'qual': qual, 'ffi': ffi}
        if disp:
            print(FFI_MAP[c_mn])

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


# for k, v in FFI_MAP.items():
#    print(k, v)

with open(TARGET_TMP, 'r') as C, open(TARGET_CPP, 'w') as CPP:
    for l in C.readlines():
        for k, v in FFI_MAP.items():
            l = l.replace(k, v['ffi'])
        l = l.replace(FFI_MARK, CLASS_SEPARATOR)
        l = l.replace('static string ', 'static std::string ')
        l = l.replace('static wstring ', 'static std::wstring ')
        CPP.write(l)
#
