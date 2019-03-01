import sys
import reader, printer
from maldata import _MalData



repl_env = {'+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: int(a/b)}



def READ(txt):
    ast = reader.read_str(txt)
    return ast

def EVAL(ast, env):

    if ast.type != "LIST": return eval_ast(ast, env)
    elif len(ast.val) == 0: return ast

    type0 = ast.val[0].type

    if type0 == "def!":
        pass
    else:
        new_ast = eval_ast(ast, env)
        l = new_ast.val
        f, args = l[0], l[1:]
        res = f(*[x.val for x in args])  # apply
        return _MalData("INT", res)
        #print(type0, '--------')


def eval_ast(ast, env):
    if ast.type == "SYMBOL":
        key = ast.val
        if not key in env:
            raise Exception('no key for env:', key)
        f = env[key]
        print('fff', f)
        return f
    elif ast.type == "LIST":
        data = tuple([EVAL(x, env) for x in ast.val])
        return _MalData("LIST", data)
    else:
        return ast


def PRINT(ast):
    txt = printer.pr_str(ast)
    return txt

def rep(x, env=repl_env):
    x = READ(x)
    x = EVAL(x, env)
    x = PRINT(x)
    print(x)
    return x


"""
if __name__=='__main__': 
    try:
        while True:
    #        print("", end='')
            #print('>', end='')
            #sys.stdout.flush()
            #x = sys.stdin.readline()
            x = input('user> ')
            rep(x)

    except KeyboardInterrupt:
        pass

"""
rep('(+ 2 3)')