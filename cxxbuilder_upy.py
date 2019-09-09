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

    with open("build/{}.json".format((lib)), 'r') as jsonf:
        code = json.loads(jsonf.read())

    # platform dependant
    clib = "lib{}_cni.so".format((lib))

    def ffimap(ffi_name):
        global RETURN_TYPE_FIRST
        if RETURN_TYPE_FIRST:
            func, ret, args = ffi_name.rsplit('_', 2)
        else:
            func, args, ret = ffi_name.rsplit('_', 2)
        return func, ret, args

    # FIXME: use readelf tools and wasm tools
    # for func in os.popen(f"nm --demangle --defined-only --dynamic {clib} |grep '. T .*_._.*$'|cut -d' ' -f3"):
    for func in os.popen("nm -C build/{} |grep '. T .*_*_.*$'|cut -d' ' -f3".format((clib))):
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
        print('dlopen failed on {}'.format((clib)))
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
        lot = []
        for cn in ck:
            if p == len(cls[cn]['bases']):
                lot.append(cn)

        lot.sort()
        forward_decl.extend(lot)

    print(forward_decl)

    code['forward_decl'] = sort_inheritance(code, forward_decl)

    return code


def sort_inheritance(code, fwd):
    def bases(cn):
        return list(cls[cn]['bases'])

    # fwd = code['forward_decl']

    cls = code['classes']

    first = 0
    for cn in fwd:
        if len(bases(cn)):
            break
        first += 1

    unsorted = True
    slot = ''

    while first < len(fwd):
        tosort = fwd[first]
        parents = bases(fwd[first])
        while parents:
            for i in range(first):
                if fwd[i] in parents:
                    parents.remove(fwd[i])
            else:
                if len(parents):
                    unsorted = True
                    slot = parents.pop(0)
                    print(tosort, 'wrong position vs', slot)
                    break
        else:
            first += 1

        if unsorted:
            good = fwd.index(slot)
            fwd.insert(good + 1, tosort)
            fwd.pop(first)
            unsorted = False

    return fwd


def handle_return_type(indent, call, *args):
    opening = ""
    closing = ""
    rt = ""
    return """{}return {}{}{}{}""".format((' '*indent), (rt), (opening), (call), (closing))


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
                """{}# enum {}
"""
.format(("    "*indent), (enum_name))            )

            for enum in enums:
                write("""{}{} = const({})""".format(("    "*indent), (enum[0]), (enum[1])))

            write("\n")

    CODE.update(dlopen(TARGET))

    lib = CODE['lib']

    forward_decl = CODE['forward_decl']

    has_main_enum = forward_decl[0] == ''

    if has_main_enum:
        forward_decl.pop(0)

    write(
        """# upy

import sys


if not '.' in sys.path: sys.path.insert(0,'.')
import interrogator.uplusplus as cxx

extern = cxx.cstructs.decl.append"""
.format()    )

    classes = CODE['classes']

    for cn in forward_decl:
        write("extern('{}') # {}".format((cn), (', '.join(classes[cn]['bases']))))

    write("del extern\n")

    if has_main_enum:
        enums(classes[''], indent=0)

    indent = 1

    for cn in forward_decl:
        ancestor = 'cxx.cplusplus'
        if len(classes[cn]['bases']):
            ancestor = ', '.join(classes[cn]['bases'])

        write(
            '''
class {}({}):

    c = cxx.cstructs()
    c.register("{}", "{}", """{}""")
'''
.format((cn), (ancestor), (cn), (TARGET), (lib))        )
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
                    write("{}c.ct['ctor'] = [".format(('    '*indent)))
                else:
                    write("{}c.ct['{}'] = [".format(('    '*indent), (func)))

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

                    cffi = "('{}', '{}', '{}')".format((ret), (ffi_name), (args))

                    # kw arguments ?
                    write("{}    ('{}', {}, {}, {}, {}),".format(('    '*indent), (ct), (pret), (proto['argc']), (cffi), (proto['argt'])))

                write("{}]".format(('    '*indent)))

            write("")
            return fnlist

        write("    # ctor/dtor\n")

        dump(classes[cn], 's', ctor=1)

        write("    # classmethod type calls\n")

        for cm in dump(classes[cn], 's', ctor=0):
            write(
                """{}@classmethod
{}def {}(cls, *args,**kw):
{}    return ( cls.c.get('{}', None) or cls.c.call({}, '{}', None) )(*args,**kw)
"""
.format(('    '*indent), ('    '*indent), (cm), ('    '*indent), (cm), (cn), (cm))            )

        write("    # instance method type calls\n")

        dump(classes[cn], 'd', ctor=0)

        write(
            """
{}# c++ instance methods

{}def __del__(self):
{}    self.c.destroy(self)

{}def __getattr__(self, attr):
{}    return self.c.get(attr,None) or  self.c.call({}, attr, self)

{}.c.link({})

"""
.format(('    '*indent), ('    '*indent), ('    '*indent), ('    '*indent), ('    '*indent), (cn), (cn), (cn))        )

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


        print('framework=', E.get_wframe() )


        np = E.load_model( "model.bam" )

        print("np","=",np)

        E.attach(np)


        Vec3 = LVecBase3f


        v3 = Vec3(0.01, 42.01, 0.01)
        print("Vec3=", v3)


        np.set_pos( v3 )

        v3 = Vec3(2.0, 2.0, 2.0)
        print( v3, v3.get_x() , v3.get_y(), v3.get_z() )
        np.set_scale( v3 )


        # feed the monkey
        GeomTriangles.c.bases.append( GeomPrimitive )

        #Geom.UH_static = 3
        #GeomT.c.bases.append( GeomTriangles )
        #GeomT.c.bases.append( GeomPrimitive )


        def Cube(size=1.0, geom_name="CubeMaker", gvd_name="Data", gvw_name="vertex"):

            format = GeomVertexFormat.get_v3()
            print("GeomVertexFormat.format =",format)

            data = GeomVertexData(gvd_name, format, GeomEnums.UH_static )
            print("GeomVertexData=", data)


            cthr = Thread.get_current_thread()
            print('CurrentThread=', cthr )

            #cxx.TRACE=1
            # BUG
            #vertices = GeomVertexWriter(data,addr gvw_name)
            vertices = E.new_GeomVertexWriter( data, gvw_name);
            cxx.TRACE=0

            print("GeomVertexWriter=", vertices)

            size = float(size) / 2.0
            vertices.add_data3f(-size, -size, -size)
            vertices.add_data3f(+size, -size, -size)
            vertices.add_data3f(-size, +size, -size)
            vertices.add_data3f(+size, +size, -size)
            vertices.add_data3f(-size, -size, +size)
            vertices.add_data3f(+size, -size, +size)
            vertices.add_data3f(-size, +size, +size)
            vertices.add_data3f(+size, +size, +size)

            #triangles = GeomTriangles(GeomEnums.UH_static)
            triangles = E.new_GeomTriangles()

            print("triangles=",triangles)


            def add_quad(v0, v1, v2, v3):
                triangles.add_vertices(v0, v1, v2)
                triangles.add_vertices(v0, v2, v3)
                #
                #BUG
                #triangles.close_primitive()
                cxx.TRACE = 1
                E.close_primitive(triangles)
                cxx.TRACE = 0

            add_quad(4, 5, 7, 6)  # Z+
            add_quad(0, 2, 3, 1)  # Z-
            add_quad(3, 7, 5, 1)  # X+
            add_quad(4, 6, 2, 0)  # X-
            add_quad(2, 6, 7, 3)  # Y+
            add_quad(0, 1, 5, 4)  # Y+

            geom = Geom(data)
            print("Geom=",geom)

            cxx.TRACE = 1

# BUG geom ptr not converted
            E.add_primitive( geom, triangles )
            #geom.add_primitive(triangles)
            cxx.TRACE = 0

            print("geom=",geom)

            node = GeomNode(geom_name)
            node.add_geom(geom)
            return NodePath(node)


        cube = Cube(size=1.0)



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
