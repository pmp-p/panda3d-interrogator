import os
import pandac
from panda3d.interrogatedb import *

DBG = 0


def translateTypeName(name, mangle=True):
    # Equivalent to C++ classNameFromCppName
    class_name = ""
    bad_chars = "!@#$%^&*()<>,.-=+~{}? "
    next_cap = False
    first_char = mangle

    for chr in name:
        if (chr == '_' or chr == ' ') and mangle:
            next_cap = True
        elif chr in bad_chars:
            if not mangle:
                class_name += '_'
        elif next_cap or first_char:
            class_name += chr.upper()
            next_cap = False
            first_char = False
        else:
            class_name += chr

    return class_name


def translated_type_name(type, scoped=True):
    while interrogate_type_is_wrapped(type):
        if interrogate_type_is_const(type):
            return 'const ' + translated_type_name(interrogate_type_wrapped_type(type))
        else:
            type = interrogate_type_wrapped_type(type)

    typename = interrogate_type_name(type)
    if typename in ("PyObject", "_object"):
        return "object"
    elif typename == "PN_stdfloat":
        return "float"
    elif typename == "size_t":
        return "int"

    if interrogate_type_is_atomic(type):
        token = interrogate_type_atomic_token(type)
        if token == 7:
            return 'str'
        elif token == 8:
            return 'long'
        elif token == 9:
            return 'NoneType'
        else:
            return typename

    if not typename.endswith('_t'):
        # Hack: don't mangle size_t etc.
        typename = translateTypeName(typename)

    if scoped and interrogate_type_is_nested(type):
        return translated_type_name(interrogate_type_outer_class(type)) + '::' + typename
    else:
        return typename


def process_enums(c, type, name, indent):
    enums = {}
    enums[name] = []
    docstrings = []

    for i_value in range(interrogate_type_number_of_enum_values(type)):
        docstring = interrogate_type_enum_value_comment(type, i_value)
        key = interrogate_type_enum_value_name(type, i_value)

        docstring = docstring.replace('// ', '')
        docstring = docstring.replace('\n', f"\n{'    '*indent}# ")

        docstrings.append((key, docstring))
        value = interrogate_type_enum_value(type, i_value)
        enums[name].append((key, value))

    enums[name].sort(key=lambda x: x[0])
    if DBG:
        if nesting:
            print(f"\n{'    '*indent}class {name}:\n")
        else:
            print(f"\n{'    '*indent}# {name}:\n")

        doc = 0
        while len(docstrings):
            key, docstring = docstrings.pop(0)
            if docstring:
                doc = 1
                if DBG:
                    print(f"{'    '*indent}# {key} : {docstring}")

        if doc:
            print()

        for (key, value) in enums[name]:
            print(f"{'    '*(indent+nesting)}{key} = const({value})")

        if nesting:
            print(f"{'    '*indent}{name}= {name}")

    c['enums'].update(enums)


def process_nested(c, type, name, indent=1):
    nesting = 0

    if interrogate_type_is_enum(type):
        process_enums(c, type, name, indent)


def process_class(c, type, used_class):
    typename = translated_type_name(type, scoped=False)
    derivations = []

    for n in range(interrogate_type_number_of_derivations(type)):
        deriv = interrogate_type_get_derivation(type, n)
        ttn = translated_type_name(deriv)
        derivations.append(ttn)
        if not ttn in used_class:
            used_class.append(ttn)

    c['bases'].extend(list(derivations))

    if not len(derivations):
        derivations += ['cpp']
    if DBG:
        print()
        print(f"class {typename}({', '.join(derivations)}):")

    for i_ntype in range(interrogate_type_number_of_nested_types(type)):
        ntype = interrogate_type_get_nested_type(type, i_ntype)
        ntype_name = interrogate_type_name(ntype)
        process_nested(c, ntype, ntype_name)


#    for i_method in range(interrogate_type_number_of_constructors(type)):
#        ctor = interrogate_type_get_constructor(type, i_method)
#        ctor_name = interrogate_function_name(ctor)
#        print('    ctor:', ctor_name)

#    for i_method in range(interrogate_type_number_of_methods(type)):
#        print('processFunction(handle,', interrogate_type_get_method(type, i_method))

#    for i_method in range(interrogate_type_number_of_make_seqs(type)):
#        print('print("list", translateFunctionName(interrogate_make_seq_seq_name(interrogate_type_get_make_seq(type, i_method))), "();", file=handle)')

#    for i_element in range(interrogate_type_number_of_elements(type)):
#        elem = interrogate_type_get_element(type, i_element)
#        elem_name = interrogate_element_name(elem)
#        print('processElement(handle,', elem_name)


def process_in(fname, source):
    used_class = []

    interrogate_request_database(fname)
    for i_type in range(interrogate_number_of_global_types()):
        type = interrogate_get_global_type(i_type)
        cn = interrogate_type_name(type)
        decl = source['classes'].get(cn, None)
        if decl:
            process_class(decl, type, used_class)
        else:
            if interrogate_type_is_enum(type):
                # a global enum
                process_enums(source['classes'][''], type, cn, 0)

    for decl_class in source['classes'].keys():
        if decl_class in used_class:
            used_class.remove(decl_class)

    if len(used_class):
        print("\nmissing def in .N :")
        for uc in used_class:
            print(f"forcetype {uc}")
        print()


# Determine the path to the interrogatedb files
pandac_dir = os.path.dirname(pandac.__file__)

interrogate_add_search_directory('.')
interrogate_add_search_directory(os.path.join(pandac_dir, "input"))
