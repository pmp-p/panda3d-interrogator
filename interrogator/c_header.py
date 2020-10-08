from .utils import qualmove, iter_name_class


# fmt: off

basict = "void,char,short,int,long,float,double,long,byte,bool".split(',')
basict.extend("std::size_t,wchar_t,std::streamsize,time_t".split(','))

ptypes = []

h_types = {
    'uint32_t'      : 'unsigned int',
#   'PN_stdfloat'  : 'float',
    'wchar_t const': 'const char',
    'char * const'  : 'const char',
    'vector_uchar' : 'unsigned char',
    'char * PointerTo< WindowFramework > const' : 'const char',
}
blacklist = {
    'GeomNode::Geoms' : None,
}


# fmt: on


# FIXME: tokenize


def CARG(cpp):
    global h_types
    cpp = cpp.replace('::', '$_')

    # f(Filename &&from)
    cpp = cpp.replace(' &&', ' *')

    for ptr_to in ('PointerTo< ', 'pvector< ', 'set< '):
        if cpp.find(ptr_to) >= 0:
            cpp = cpp.split('> ', 1)[-1]
            cpp = 'char *' + cpp.split(' *', 1)[-1]

    # cpp = cpp.replace(' * * ', ' * ')

    for pre in '( ':
        for k, v in h_types.items():
            cpp = cpp.replace(f'{pre}{k} ', f'{pre}{v} ')
        askip = 0

    return cpp, askip


def fix_c_types(decl, type_only=False):
    if type_only:
        arg = CARG(decl)[0]
        if len(arg) and not arg[-1] in '&* ':
            arg += ' '
        return arg

    return CARG(decl)[0]


def record_types(pt):
    pt, askip = CARG(pt)
    if askip:
        return

    pt = pt.strip(' *&')
    if not pt:
        return

    for atom in pt.split(' '):
        atom = atom.strip(' *&<>')
        if atom:
            if atom in basict:
                continue
            if atom in ['signed', 'unsigned', 'const']:
                continue

            if atom.startswith('std$_'):
                continue

            if not atom in ptypes:
                ptypes.append(atom)


def c_header(H, source):
    H.write(
        """
#include <stdio.h>
#include <stdbool.h>
#include <time.h>

#define PT char
#define PN_stdfloat float

#define wchar_t char
//#define string char const

#define std$_size_t unsigned int
#define std$_streamsize int

#define std$_string char
#define std$_wstring char
#define std$_fstream char
#define std$_ifstream char
#define std$_istream char
#define std$_ofstream char
#define std$_ostream char

"""
    )

    for pt in source['btypes']:
        record_types(pt)

    ck = list(source['classes'].keys())
    ck.sort()

    for cls in ck:
        disp = 0
        for proto in source['classes'][cls]['proto']:
            for idx, arg in enumerate(proto['args']):
                if arg == 'void':
                    continue
                atype, aname = arg.rsplit(' ', 1)
                atype, aname = qualmove(atype, aname)

                if disp:
                    print(atype, aname)

                record_types(atype)

    enums = []



    for cn, co in iter_name_class(source):
        h_types[cn] = 'char'
        if not cn in ptypes:
            ptypes.append(cn)

        for enum_name in co['enums'].keys():
            if enum_name:
                h_types[enum_name] = 'int'

        # for enum_name,enums in co['enums'].items():
        # for enum in enums:
        #    h_types[enum[0]]='int'

    ptypes.sort()

    for bad in ('', 'PT', 'PN_stdfloat', 'string'):
        if bad in ptypes:
            ptypes.remove(bad)

    for pt in ptypes:
        H.write(f"#define {pt} {h_types.get(pt,'char')}\n")

    H.write("\n")

    for cls in ck:
        print(f"// {cls}\n", file=H)
        protocnt = 0

        for proto in source['classes'][cls]['proto']:


            protocnt += 1
            ex_type, ex_decl = proto['extern']

            ex_type = fix_c_types(ex_type)
            ex_name = proto['demangled'].replace('$_$', '$%s$' % protocnt)
            proto['indexed'] = ex_name

            ex_decl = fix_c_types(ex_decl.replace('$_$', '$%s$' % protocnt))
            ffi_args = []

            is_void = False
            if proto['argc']:
                argv = list(proto['c_argv'])
                for idx, arg in enumerate(argv):
                    arg = fix_c_types(arg, type_only=True)
                    ffi_args.append(arg.strip().replace(' ','-'))

                    if proto['ct'] == 's':
                        argv[idx] = f"{arg}{proto['argn'][idx]}"
                        continue

                    if idx:
                        argv[idx] = f"{arg}{proto['argn'][idx-1]}"
                        continue

                    argv[0] = f"{arg}self"
            else:
                # C(self) == C++(void)
                if proto['ct']=='d':
                    ffi_args = ['pointer']
                    argv = [ proto['c_argv'][0]+'self' ]
                else:
                    ffi_args = ['void']
                    argv = ['void']
                    is_void = True

            cpp = ', '.join(proto['args'])
            c = ', '.join(proto['c_argv'])
            if 0: #proto['c_ref'].count('Engine'):
                #Engine_C_ctor_p_v
                import json
                print( json.dumps(proto,indent=4) )
                #raise SystemExit

            print(f"// C++ {proto['mangled']}({cpp}) ==> {proto['c_ref']}({c})", file=H)
            print(f"extern {ex_type} {ex_name}({', '.join(argv)});", file=H)
            CNI(H, proto, ex_type, ex_name, ffi_args, is_void)
            print("", file=H)

        print("", file=H)

#


# fmt: off



FFI_TYPE_MAP = {
    "pointer":"p",
    "char-*" : "p",
    "void": "v",
    "char-const-*": "s",
    "wchar_t-const-*" :  "s",
    "const-char-*": "s",
    "char_t-const-*" :  "s",
    "int": "i",
    "long": "l",
    "enum": "i",
    "float": "f",
    "double": "d",
    "uint8_t": "B",
    "uint16_t": "H",
    "uint32_t": "I",
    "ssize_t": "l",
    "_Bool": "B",
    "bool": "B",
    "signed-char": "b",
    "char-signed": "b",
    "unsigned-char": "B",
    "char-unsigned": "B",
    "short": "h",
    "unsigned-short": "H",
    "unsigned-short-int" : "H",
    "short-unsigned": "H",
    "short-unsigned-int": "H",
    "unsigned-int": "I",
    "int-unsigned": "I",
    "unsigned-long": "L",
    "long-unsigned": "L",
    "long-long": "q",
    "unsigned-long-long": "Q",
    "long-long-unsigned": "Q",

    "InternalName-const-*":"s",
    'CPT_InternalName-*' : "s",
    "PN_stdfloat": "f",
    "std$_size_t" : "l",
    "std$_streamsize": "l",
    "std$_wstring" : "s",
    "std$_string" : "s",

}

COLLISIONS = []



def CNI(H, proto, rt, target, ffi_args, is_void):

    rt = rt.strip().replace(' ','-').replace('**','*').strip()

    proto['c_rt'] = rt

    rt = FFI_TYPE_MAP.get(rt,'p')

    argt = []

    for a in ffi_args:
        argt.append( FFI_TYPE_MAP.get(a,'p') )

    if proto['ctor']:
        cni = proto['demangled'].replace(f"$_${proto['cn']}", '_C_ctor')
    else:
        cni = proto['demangled'].replace('$_$', '_C_')

    args = ''.join(argt)

    proto['cni_rt'] = rt

    if is_void and args=='v':
        # 'v' => modffi.c:355: ffifunc_call: Assertion `n_args == self->cif.nargs' failed.
        proto['cni_args'] = ''
    else:
        proto['cni_args'] = args



    cni = f"{cni}_{rt}_{args}"

    if cni in COLLISIONS:
        print(f"// COLLISION : {cni} {target}", file=H)
        skip = 1
        while cni in COLLISIONS:
            cni = f"{cni}_{skip}_{rt}_{args}"
            skip += 1
        proto['cni']=cni
    else:
        proto['cni'] = cni
        print(f"""
#if INDEX
#define {cni} {target}
#endif""", file=H)

    COLLISIONS.append(cni)


























































#











# fmt: on
