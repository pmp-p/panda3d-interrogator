# upy

# STM GC
#   https://bitbucket.org/pypy/stmgc/src/default/

# ffi
#   https://pycopy.readthedocs.io/en/latest/library/ffi.html

# jni
#   https://github.com/pfalcon/pycopy/blob/pfalcon/ports/unix/modjni.c

# llvm
#   https://github.com/pfalcon/ullvm


# https://github.com/pfalcon/awesome-micropython


FFI_MARK = '_C_'
CNI = 1

RETURN_TYPE_FIRST = 1

DBG = 0


import os
import sys

try:
    import uctypes
except:
    print('CPY')

try:
    import ffi
except:
    print("FIXME: cpython")


try:
    import ujson as json
except:
    import json


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

CTP = 0
RET = 1
VAR = 2
FFI = 3


def dlopen(lib):

    with open(f"build/{lib}.json", 'r') as jsonf:
        code = json.loads(jsonf.read())

    # platform dependant
    clib = f"lib{lib}_cni.so"

    def ffimap(ffi_name):
        global RETURN_TYPE_FIRST
        if RETURN_TYPE_FIRST:
            func, ret, args = ffi_name.rsplit('_', 2)
        else:
            func, args, ret = ffi_name.rsplit('_', 2)
        return func, ret, args

    # FIXME: use readelf tools and wasm tools
    # for func in os.popen(f"nm --demangle --defined-only --dynamic {clib} |grep '. T .*_._.*$'|cut -d' ' -f3"):
    for func in os.popen(f"nm -C build/{clib} |grep '. T .*_*_.*$'|cut -d' ' -f3"):
        ffi_name = func.strip()
        if ffi_name.find(FFI_MARK) < 1:
            if DBG:
                print("N/I: globals", func, end='')
            continue

        try:
            func, ret, args = ffimap(ffi_name)
            cls, func = func.split(FFI_MARK, 1)
            code.setdefault(cls, {})
            code[cls].setdefault(func, [])
            code[cls][func].append((code['callmap'].get(ffi_name, 'd'), ret, args, ffi_name))

            if DBG:
                print(cls, '.', func, args, '->', ret)
        except:
            if DBG:
                print("N/I:", func, end='')

    print("Loading native lib", clib, file=sys.stderr)

    try:
        lib = ffi.open(clib)
    except Exception as e:
        sys.print_exception(e)
        print(f'dlopen failed on {clib}')
        raise SystemExit

    code['lib'] = clib
    del code['btypes']

    forward_decl = []
    cls = code['classes']
    ck = list(cls.keys())
    ck.sort()
    mx = 0
    for cn in ck:
        mx = max(mx, len(cls[cn]['bases']))

    print('MAX PARENTS =', mx)
    for p in range(mx + 1):
        for cn in ck:
            if p == len(cls[cn]['bases']):
                forward_decl.append(cn)

    forward_decl.sort()
    print(forward_decl)

    code['forward_decl'] = forward_decl

    return code


def handle_return_type(indent, call, *args):
    opening = ""
    closing = ""
    rt = ""
    return f"""{' '*indent}return {rt}{opening}{call}{closing}"""


def is_tor(func):
    return func.startswith('ctor') or func.startswith('dtor')


def build(TARGET):
    global CODE, DBG

    OUT_FILE = open('build/%s.py' % TARGET, 'w')

    def write(*argv, **kw):
        global DBG
        if DBG:
            print(*argv, **kw)
        kw['file'] = OUT_FILE
        print(*argv, **kw)

    def ret_cpp(ret, ffi_name):
        pret = "'%s'" % ret
        if ret == 'p':
            if ffi_name in forward_decl:
                pret = forward_decl.index(ffi_name)
        return pret, ffi_name

    def enums(cls, indent=0):
        for enum_name, enums in cls['enums'].items():
            write(
                f"""{"    "*indent}# enum {enum_name}
"""
            )

            for enum in enums:
                write(f"""{"    "*indent}{enum[0]} = const({enum[1]})""")

            write("\n")

    #

    #

    #

    #

    CODE.update(dlopen(TARGET))

    lib = CODE.pop('lib')

    # callmap = CODE.pop('callmap')
    # retmap = CODE.pop('retmap')

    forward_decl = CODE.pop('forward_decl')

    has_main_enum = forward_decl[0] == ''

    if has_main_enum:
        forward_decl.pop(0)

    write(
        f"""# upy

import sys


if not '.' in sys.path: sys.path.insert(0,'.')
import interrogator.uplusplus as cxx

extern = cxx.cstructs.decl.append"""
    )
    for decl in forward_decl:
        write(f"extern('{decl}')")

    write("del extern\n")

    classes = CODE['classes']

    if has_main_enum:
        enums(classes[''], indent=0)

    indent = 1

    for cn in forward_decl:
        ancestor = 'cxx.cplusplus'

        write(
            f'''
class {cn}({ancestor}):

    c = cxx.cstructs()
    c.register("{cn}", "{TARGET}", """{lib}""")
'''
        )
        enums(classes[cn], indent=1)
        # write("# ============== ENUM OFF ====================")

        def dump(cls, ct, ctor=0):
            global CNI

            fnlist = []

            for proto in cls['proto']:
                if proto['ctor'] != ctor:
                    continue

                if proto['ct'] != ct:
                    continue

                if not proto['fn'] in fnlist:
                    fnlist.append(proto['fn'])
            fnlist.sort()

            for func in fnlist:
                if ctor:
                    write(f"{'    '*indent}c.ct['ctor'] = [")
                else:
                    write(f"{'    '*indent}c.ct['{func}'] = [")

                for proto in cls['proto']:
                    if proto['fn'] != func:
                        continue

                    ret = proto['cni_rt']
                    pret, cret = ret_cpp(ret, proto['rt'])

                    args = proto['cni_args']
                    if CNI:
                        ffi_name = proto['cni']
                    else:
                        ffi_name = proto['indexed']

                    # cffi = f"c.lib.func('{ret}','{ffi_name}','{args}')"
                    cffi = f"('{ret}', '{ffi_name}', '{args}')"
                    write(f"{'    '*indent}    ('{ct}', {pret}, {proto['argc']}, {cffi}, {proto['argn']}),")

                write(f"{'    '*indent}]")

            # write("\n#", fnlist)
            write("")
            return fnlist

        write("    # ctor/dtor\n")

        dump(classes[cn], 's', ctor=1)

        write("    # classmethod type calls\n")

        for cm in dump(classes[cn], 's', ctor=0):
            write(
                f"""{'    '*indent}@classmethod
{'    '*indent}def {cm}(cls, *args,**kw):
{'    '*indent}    return ( cls.c.get('{cm}', None) or cls.c.call({cn}, '{cm}', None) )(*args,**kw)
"""
            )

        write("    # instance method type calls\n")

        dump(classes[cn], 'd', ctor=0)

        write(
            f"""
{'    '*indent}# c++ instance methods

{'    '*indent}def __del__(self):
{'    '*indent}    self.c.destroy(self)

{'    '*indent}def __getattr__(self, attr):
{'    '*indent}    return self.c.get(attr,None) or  self.c.call({cn}, attr, self)

{cn}.c.link({cn})

"""
        )

    if TARGET == 'upanda3d':
        write(
            """
if __name__ == '__main__':
    import os
    import gc
    import time
    import uctypes
    REFC = cxx.REFC

    def test():


        for proto in Engine.c.ct['ctor']:
            print("C++ class constructor", proto)

        E = Engine()

        print('engine      ',E)
        C = E.__class__( iptr=E )
        print('engine(copy)',C)

        # a dumb test that should say 42
        print('hello',E.HelloEngine())

        print('version','=', E.get_version_string())

        E.build()

        cxx.TRACE=1
        print('framework=', E.get_wframe() )


        np = E.load_model( "model.bam" )

        print("np","=",np)

        E.attach(np)

        cxx.TRACE=0

        Vec3 = LVecBase3f

        if 0:
            # feed the monkey
            Geom.UH_static = 3
            GeomTriangles.c.bases.append( GeomPrimitive )
            #GeomT.c.bases.append( GeomTriangles )
            #GeomT.c.bases.append( GeomPrimitive )



        def Cube(size=1.0, geom_name="CubeMaker", gvd_name="Data", gvw_name="vertex"):




            format = GeomVertexFormat.get_v3()
            print("GeomVertexFormat.format =",format)

            data = GeomVertexData(gvd_name, format, Geom.UH_static )
            print("GeomVertexData=", data)


            cthr = Thread.get_current_thread()
            print('CurrentThread=', cthr )


            #vertices = GeomVertexWriter(data, gvw_name)
            #vertices = GeomVertexWriter( cptr=

            vertices = E.new_GeomVertexWriter( data, gvw_name);
            vertices = GeomVertexWriter( cptr= vertices )
            print("GeomVertexWriter=", vertices)

            triangles = GeomTriangles(Geom.UH_static)

            print("triangles=",triangles)



            size = float(size) / 2.0
            vertices.add_data3f(-size, -size, -size)
            vertices.add_data3f(+size, -size, -size)
            vertices.add_data3f(-size, +size, -size)
            vertices.add_data3f(+size, +size, -size)
            vertices.add_data3f(-size, -size, +size)
            vertices.add_data3f(+size, -size, +size)
            vertices.add_data3f(-size, +size, +size)
            vertices.add_data3f(+size, +size, +size)


            if 0:
                def add_quad(v0, v1, v2, v3):
                    triangles.add_vertices(v0, v1, v2)
                    triangles.add_vertices(v0, v2, v3)
                    cxx.TRACE = 1
                    #triangles.close_primitive()
                    E.close_primitive(triangles)

                add_quad(4, 5, 7, 6)  # Z+
                add_quad(0, 2, 3, 1)  # Z-
                add_quad(3, 7, 5, 1)  # X+
                add_quad(4, 6, 2, 0)  # X-
                add_quad(2, 6, 7, 3)  # Y+
                add_quad(0, 1, 5, 4)  # Y+

            geom = Geom(data)
            print("Geom=",geom)

            cxx.TRACE = 1
            #geom.add_primitive(triangles)
            E.add_primitive( geom, triangles )


            print("geom=",geom)

            node = GeomNode(geom_name)
            node.add_geom(geom)
            return NodePath(node)


        if 0:
            cube = Cube(size=1.0)

        if 0:

            v3 = Vec3(0.01, 42.01, 0.01)

            np.set_pos( v3 )

            v3 = Vec3(2.0, 2.0, 2.0)
            print( v3, v3.get_x() , v3.get_y(), v3.get_z() )
            np.set_scale( v3 )



        while E.is_alive():
            E.step()
            gc.collect()
            time.sleep(.016)

        print("C++ engine requested exit")
        del E
        print("deleting copy")
        del C

    print("--- test3 with refcounting ----")
    test()
    del test
    gc.collect()
    gc.collect()

    cxx.gc()

"""
        )

    try:
        OUT_FILE.close()
    except:
        pass


if __name__ == '__main__':
    build('upanda3d')


#
