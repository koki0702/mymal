from maldata import _MalData
import printer


def _mal(d):
    if isinstance(d, bool) and d == True:
        return _MalData("TRUE")
    elif isinstance(d, bool) and d == False:
        return _MalData("FALSE")
    elif isinstance(d, int):
        return _MalData("INT", d)


def prn(*args):
    ret = []
    for ast in args:
        ret.append(printer.pr_str(ast, True))
    txt = " ".join(ret)
    print(txt)
    return _MalData("NIL")


def println(*args):
    ret = []
    for ast in args:
        ret.append(printer.pr_str(ast, False))
    txt = " ".join(ret)
    print(txt)
    return _MalData("NIL")

def _eq(a,b):
    S = ("LIST", "VECTOR")

    if a.type in S and b.type in S:
        if len(a.val) != len(b.val): return False
        if len(a.val) == 0 and len(b.val) == 0: return True

        for _a, _b in zip(a.val, b.val):
            if not _eq(_a, _b): return False
        return True

    if a.type != b.type: return False
    elif a.val == b.val:
        return True
    else:
        return False

def eq(a,b):
    flg = _eq(a,b)
    return _mal(flg)


def _P(f):
    def g(*args):
        return _mal(f(*[x.val for x in args]))
    return _MalData("FUNCTION", g)

def _F(f):
    return _MalData("FUNCTION", f)

def _prs(*args):
    ret = []
    for ast in args:
        ret.append(printer.pr_str(ast))
    return _MalData("STRING", " ".join(ret))


def _str(*args):
    ret = []
    for ast in args:
        ret.append(printer.pr_str(ast, False))
    return _MalData("STRING", "".join(ret))

def _list(*args):
    return _MalData("LIST", args)

ns = {
'+': _P(lambda a,b: a+b),
'-': _P(lambda a,b: a-b),
'*': _P(lambda a,b: a*b),
'/': _P(lambda a,b: int(a/b)),

'list': _F(_list),
'list?': _F(lambda *x: _mal(x[0].type == "LIST")),
'empty?': _F(lambda *x: _mal(len(x[0].val) == 0)),
'count': _F(lambda *x: _mal(len(x[0].val) if x[0].type != "NIL" else 0)),
'=': _F(eq),

'<': _P(lambda *x: x[0] < x[1]),
'<=': _P(lambda *x: x[0] <= x[1]),
'>': _P(lambda *x: x[0] > x[1]),
'>=': _P(lambda *x: x[0] >= x[1]),

'prn': _F(prn),
'println': _F(println),
'pr-str': _F(_prs),
'str': _F(_str),
}
