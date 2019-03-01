from maldata import _MalData


def _escape(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')


def pr_str(ast, print_readably=True):
    _p = print_readably
    if ast.type == "LIST":
        return "(" + " ".join([pr_str(x, _p) for x in ast.val]) + ")"
    elif ast.type == "VECTOR":
        return "[" + " ".join([pr_str(x, _p) for x in ast.val]) + "]"
    elif ast.type == "HASH":
        ret = []
        obj = ast.val
        for k in obj.keys():
            ret.extend((pr_str(k, _p), pr_str(obj[k],_p)))
        return "{" + " ".join(ret) + "}"
    elif ast.type == "SYMBOL":
        return ast.val
    elif ast.type == "INT":
        return str(ast.val)
    elif ast.type == "STRING":
        #if len(obj) > 0 and obj[0] == types._u('\u029e'):
        #    return ':' + obj[1:]
        if print_readably:
            return '"' + _escape(ast.val) + '"'
        else:
            return ast.val
    elif ast.type == "KEYWORD":
        return ast.val.replace('\u029e', ':')
    elif ast.type == "TRUE":
        return "true"
    elif ast.type == "FALSE":
        return "false"
    elif ast.type == "NIL":
        return "nil"

    else:
        raise Exception("No Data Type:", ast.type)

