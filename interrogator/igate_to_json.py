import sys

try:
    import ubinascii as binascii
except ImportError:
    import binascii


from .utils import qualmove


DBG = 0
TODO = 0

watchdog = True

def init_classe(source, cn):
    return source['classes'].setdefault(cn, {'bases': [], 'enums': {}, 'proto': []})


def igate_to_json(file_like):
    def extract_cpp_names(cpp_def):
        global watchdog

        if not watchdog:
            raise SystemExit

        # clean up unwanted initializer:   class(arg = init()) => class(arg = init)

        # pass 1
        begin = cpp_def.split('(',1)[0]
        end = cpp_def.rsplit(')',1)[-1]

        head = cpp_def[:len(begin)]

        # pass 2
        tail = cpp_def[len(begin)+1:-(1+len(end))]
        tail = tail.replace('(0.0, 0.0, 0.0)','()')
        tail = tail.replace('()','')


        #head, tail = cpp_def.rsplit('(', 1)

        if head.find(' ') < 0:
            cpp_type = ''
            class_func = head
        else:
            cpp_type, class_func = head.rsplit(' ', 1)

        cpp_type, class_func = qualmove(cpp_type, class_func)

        ppos = class_func.find('(')
        dpos = class_func.find('::')

        if ( (ppos>0) and (cpos < dpos)) or (dpos<0):
                print("#FIXME: not a class method", class_func)

        class_name, func_name = class_func.split('::',1)

        STATIC = 'static '
        if cpp_type.startswith(STATIC):
            cpp_type = cpp_type[len(STATIC) :]
            ct = 's'
            decal = 0
        else:
            ct = 'd'
            decal = 1

        # ctor
        ctor = 0
        if class_name == func_name:
            return_type = class_name
            ctor = 1
            # ctor are handled are static no matter what got parsed in args.
            ct = 's'
            decal = 0
        else:
            return_type = cpp_type.replace('inline','')
            return_type = return_type.replace('static','')
            return_type = return_type.replace('const','')
            return_type = return_type.replace('&','')
            return_type = return_type.replace('*','')
            return_type = return_type.replace('virtual','')
# TODO: move that in a user defined dict+func
            return_type = return_type.replace('InternalName ','')
            if return_type.find('>')>0:
                return_type = return_type.split('< ',1)[-1]
                return_type = return_type.rsplit(' >',1)[0]
            return_type = return_type.strip()
# fmt : off
            if len(return_type) and return_type[-1] in '234':
                for rt in [
                        'LPoint2','LPoint3',
                        'LVector2','LVector3','LVector4',
                        'LVecBase2','LVecBase3','LVecBase4',
                    ]:
                    return_type = return_type.replace(rt,'%sd'%rt)
# fmt : on

        args = []

        for arg in tail.rsplit(')', 1)[0].split(', '):
            args.append(arg.strip())

        argt = []
        argn = []

        disp = 0

        #if cpp_def.count('NodePath::look_at'):
        #    disp = 1

        if disp:
            print("BEGIN: [%s]" % begin)
            print("END: [%s]" % end)
            print("ARGS : %r" % args)

        if not len(args) or (args[0] == 'void'):
            pos = 0
            args = []
        else:
            pos = len(args)
            for idx, a in enumerate(args):
                if a.endswith(' &'):
                    a = a + f'arg{idx+decal}'

                try:
                    at, an = a.rsplit(' ', 1)
                    at, an = qualmove( at, an )
                    argt.append(at)
                    # param -> arg
                    an = an.replace('param','arg')

                    argn.append(an)
                except :
                    print("113:[%s]"%a, cpp_def,"args=",args)
                    watchdog = False


        if disp:
            print("ARGT :", argt)
            print("ARGN :", argn)

        return {
            'cn': class_name,
            'fn': func_name,
            'rt': return_type,
            'ct': ct,
            'ot': cpp_type,
            'args': args,
            'argn': argn,
            'argt': argt,
            'ctor': ctor,
            'argc': pos,
        }, disp


    def dump_info(cpp_def,c_def,ret):
        print("cpp :", cpp_def)
        print("c   :", c_def)
        for k, v in ret.items():
            print("    ", k, ":", v)
        print("\n\n\n")


    def extract_class(cpp_def, c_def):
        ret,disp = extract_cpp_names(cpp_def)
        try:
            #  f(void)
            if (not ret['argc']) and (ret['ct'] == 's'):
                ret['c_argv'] = []
                return ret

            cd = c_def.rsplit('(', 1)[-1]
            cd = cd.rsplit(')', 1)[0]

            c_argv = []
            for ca in cd.split(','):
                c_argv.append(ca.rsplit('param')[0].strip())

            # interrogate's fault c++ comments may have more args than C exports
            # https://github.com/panda3d/panda3d/issues/732

            if len(c_argv) and (c_argv[0]==''):
                c_argv=[]

            ret['c_argv'] = c_argv

            if ret['argc']:
                if ret['ct'] == 's':
                    while len(ret['args']) > len(ret['c_argv']):
                        ret['args'].pop()
                        ret['argt'].pop()
                        ret['argn'].pop()
                        ret['argc'] -= 1
                else:
                    while len(ret['args']) > len(ret['c_argv']) - 1:
                        ret['args'].pop()
                        ret['argt'].pop()
                        ret['argn'].pop()
                        ret['argc'] -= 1

            # interrogate's fault c++ comments may have more args than C exports
            try:
                if ret['argc']:
                    if ret['ct'] == 's':
                        assert len(ret['args']) == len(ret['c_argv'])
                    else:
                        assert len(ret['args']) == len(ret['c_argv']) - 1
            except AssertionError as e:
                sys.print_exception(e, sys.stdout)

            return ret
        finally:
            if disp:
                dump_info(cpp_def,c_def,ret)

    # default : ignore everything
    invalidate = 1
    relevant = 0
    c_block = 0

    EXPORT_FUNC = 'EXPORT_FUNC '
    btypes = []
    exports = []
    classes = {}

    SOURCE = {'export': exports, 'classes': classes, 'btypes': btypes}

    init_classe(SOURCE, '')

    def make_c_id(cpp):
        return f"{cpp['cn']}$_${cpp['fn']}"

    while 1:
        cline = file_like.readline()
        if not cline:
            break

        cline = cline.strip()

        if not relevant:

            if cline.startswith(EXPORT_FUNC):
                exp = cline[len(EXPORT_FUNC) : -1]
                head, tail = exp.split('(', 1)
                extype = head.rsplit(' ', 1)[0]

                if not extype in btypes:
                    if extype.count('*'):
                        btypes.append(extype)
                    else:
                        btypes.insert(0, extype)

                exports.append([extype, exp[1 + len(extype) :]])
                # print(exports[-1])
                continue

            if not len(cline):
                continue

        if cline.endswith('*/') or cline.startswith('/*'):
            continue

        if cline.startswith('* C wrapper for'):
            cpp_def = ""
            c_type = ""
            c_def = ""
            mangled = ""
            code = []

            relevant = 1
            invalidate = 0
            continue

        if invalidate:
            if relevant:
                if DBG:
                    print("invalidated", cline, end='')
            continue

        if not relevant:
            continue

        if relevant == 1:
            if cline.startswith('* '):
                cpp_def = cline[2:]

                if DBG:
                    print("cpp_def :", cpp_def)
            relevant = 2
            continue

        if relevant == 2:
            c_type = cline
            if DBG:
                print("c_type :", c_type)
            relevant = 3
            continue

        if relevant == 3:
            if not cline.endswith(') {'):
                print("MALFORMED IGATE FILE ') {' was expected", cline)
                continue

            c_def = cline[:-2]

            relevant = 4
            continue

        if relevant == 4:
            if cline != '}':
                code.append(f"    {cline}")
                continue

            # end of code block

            relevant = 0
            invalidate = 1

            if cpp_def.find('::') < 0:
                if TODO:
                    print("N/I: main_function :", cpp_def)
                continue

            if cpp_def.find('operator ') > 0:
                if TODO:
                    print("N/I: operator :", cpp_def)
                continue

            try:
                ret = extract_class(cpp_def, c_def)

                mangled = c_def.split('(', 1)[0]
                demangled = make_c_id(ret)

                ret['mangled'] = mangled
                ret['demangled'] = demangled

                ret['c_type'] = c_type
                ret['cpp_ref'] = cpp_def
                ret['c_ref'] = c_def.replace(mangled, demangled)
                code = '\n'.join(code).encode('utf-8')
                ret['code'] = binascii.hexlify(code).decode()

                for index, item in enumerate(exports):
                    if c_def == item[1]:
                        (et, ed) = exports.pop(index)
                        ed = ed.replace(mangled, demangled)
                        ret['extern'] = [et, ed]
                        break
                else:
                    print("NOT EXPORTED :", c_def)

                c = init_classe(SOURCE, ret['cn'])

                c['proto'].append(ret)

                if DBG:
                    print(ret)
                    print()

            except SystemExit:
                raise

            except Exception as e:
                sys.print_exception(e, sys.stderr)
                print("342:ERROR: extract_class_name:", cpp_def)
                print()

            continue

    if DBG:
        print("========= .h export list (should be empty) =========")
        for ex in exports:
            print(ex)
        print("end .h")
        print()

    return SOURCE
