fix_it = {
    'string': 'std::string',
    'wstring' : 'std::wstring',
    'set<': 'std::set<',
}

def fix_cpp_types(decl):
    for pre in '( ':
        for k,v in fix_it.items():
            decl = decl.replace('{}{} '.format((pre), (k)), '{}{} '.format((pre), (v)))
    return decl


def qualmove(t, n):
    while len(n) and (n[0] in '*&'):
        t+= n[0]
        n = n[1:]
    return t,n



def stripped_list(l):
    return list(map(str.strip, l))


ck = None


def iter_name_class(source):
    global ck
    if ck is None:
        ck = list(source['classes'].keys())
        ck.sort()
    for cn in ck:
        yield (cn, source['classes'][cn])


