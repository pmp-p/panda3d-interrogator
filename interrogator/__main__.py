CLASS_SEPARATOR = "_C_"
# RETURN_TYPE_FIRST = 1
DBG = 0


TARGET = 'build/interrogate'
TARGET_TMP = f'{TARGET}_temp.cpp'
TARGET_CPP = f'{TARGET}_wrapper.cpp'
TARGET_H = f'{TARGET}_wrapper.h'
TARGET_CNI = f'{TARGET}_cni.cpp'
TARGET_JSON = f'{TARGET}_wrapper.json'

FFI_MARK = '$'


import sys, os
import traceback
import argparse

from .utils import fix_cpp_types, iter_name_class


try:
    import ujson as json
except:
    import json

try:
    import ubinascii as binascii
except ImportError:
    import binascii


def print_exception(e, out, **kw):
    kw['file'] = out
    traceback.print_exc(**kw)


sys.print_exception = print_exception

"""
json schematic
______________

"export" :
    [
        [type,decl],
        [type,decl],
        [type,decl],
    ],

"btypes" : [type,type,],

"classes" : {
    class_name : {
        "bases" : [],

        "enums" : [],

        func_name : [
            {
                'cn': class_name,
                'fn': func_name,
                'rt': return_type,
                'ct': ct,
                'ot': cpp_type,
                'args': args,
                'ctor': ctor,
                'argc': pos,
            }
        ]
    }
}




"""


# Parameters

parser = argparse.ArgumentParser()

parser.add_argument("--built", default='/usr/local', help="panda ./built directory or /usr /usr/local")
parser.add_argument("--source", default="./lib", help="cxx/h lib folder")
parser.add_argument("--name", default="", help="target lib name")
parser.add_argument("--toolchain", default="", help="toolchain root")
parser.add_argument("--sysroot", default="", help="toolchain sysroot")

args = parser.parse_args()


from .igate_to_json import igate_to_json
from .process_in import process_in
from .c_header import c_header


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

    with open(TARGET_TMP, 'r') as FILE:
        source = igate_to_json(FILE)

    process_in("build/interrogate.in", source)

    with open(TARGET_TMP, 'r') as CXX:
        with open(TARGET_CPP, 'w') as CPP, open(TARGET_CNI, 'w') as CNI, open(TARGET_H, 'w') as H:

            # CXX lib
            while True:
                cline = CXX.readline().strip()
                if cline.startswith('EXPORT_FUNC '):
                    break
                print(cline, file=CPP)
                print(cline, file=CNI)

            ck = list(source['classes'].keys())
            ck.sort()

            for cn, cls in iter_name_class(source):

                print(f"\n// {cn}\n", file=CPP)
                idx = 0
                for proto in cls['proto']:
                    idx += 1
                    ex_type, ex_decl = proto['extern']
                    ex_decl = fix_cpp_types(ex_decl.replace('$_$', '$%s$' % idx))
                    print(f"EXPORT_FUNC {ex_type} {ex_decl};", file=CPP)

                print("", file=CPP)

            for cn, cls in iter_name_class(source):
                print(f"\n// {cn}\n", file=CPP)
                idx = 0
                for proto in cls['proto']:
                    idx += 1
                    c_proto = fix_cpp_types(proto['c_ref'].replace('$_$', '$%s$' % idx))
                    code = fix_cpp_types(binascii.unhexlify(proto['code']).decode())
                    print(
                        f"""
{proto['extern'][0]}
{c_proto} {{
{code}
}}
""",
                        file=CPP,
                    )

            # .h for C , will also fill c native interface
            c_header(H, source)

            for cn, cls in iter_name_class(source):

                print(f"\n// {cn}\n", file=CNI)
                idx = 0
                for proto in cls['proto']:
                    idx += 1
                    ex_type, ex_decl = proto['extern']
                    ex_decl = ex_decl.replace(proto['demangled'], proto['cni'])
                    ex_decl = fix_cpp_types(ex_decl)
                    print(f"EXPORT_FUNC {ex_type} {ex_decl};", file=CNI)

                print("", file=CNI)

            for cn, cls in iter_name_class(source):
                print(f"\n// {cn}\n", file=CNI)
                idx = 0
                for proto in cls['proto']:
                    idx += 1
                    c_proto = proto['c_ref'].replace(proto['demangled'], proto['cni'])
                    c_proto = fix_cpp_types(c_proto)
                    code = fix_cpp_types(binascii.unhexlify(proto['code']).decode())
                    print(
                        f"""
{proto['extern'][0]}
{c_proto} {{
{code}
}}
""",
                        file=CNI,
                    )

    with open(TARGET_JSON, 'w') as f:
        f.write(json.dumps(source, sort_keys=True, indent=4))

else:
    print(f"--source folder invalid : '{args.source}'")
