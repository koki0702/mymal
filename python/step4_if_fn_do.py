import sys, traceback
import reader, printer
from maldata import _MalData
from env import Env


repl_env = Env()

repl_env.set('+', lambda a,b: a+b)
repl_env.set('-', lambda a,b: a-b)
repl_env.set('*', lambda a,b: a*b)
repl_env.set('/', lambda a,b: int(a/b))


def READ(txt):
    ast = reader.read_str(txt)
    return ast

def EVAL(ast, env):
    if ast.type == "LIST":
        l = ast.val
        if len(l) == 0:
            return ast
        else:
            ast0 = ast.val[0]

            if ast0.type == "SYMBOL" and ast0.val == "def!":
                key = ast.val[1].val
                v = EVAL(ast.val[2], env)
                env.set(key, v)
                return v
            elif ast0.type == "SYMBOL" and ast0.val == "let*":
                let_env = Env(env)
                bidings = ast.val[1]

                for a, b in zip(bidings.val[0::2], bidings.val[1::2]):
                    key = a.val
                    v = EVAL(b, let_env)
                    let_env.set(key, v)

                return EVAL(ast.val[2], let_env)
            else:
                new_ast = eval_ast(ast, env)
                l = new_ast.val
                f, args = l[0], l[1:]
                res = f(*[x.val for x in args])  # apply
                return _MalData("INT", res)

    else:
        return eval_ast(ast, env)

def PRINT(ast):
    txt = printer.pr_str(ast)
    return txt

def rep(x, env=repl_env):
    x = READ(x)
    x = EVAL(x, env)
    x = PRINT(x)
    print(x)
    return x


def eval_ast(ast, env):
    if ast.type == "SYMBOL":
        key = ast.val
        if env.find(key) is None:
            raise Exception('no key for env:', key)
        f = env.get(key)
        return f
    elif ast.type == "LIST":
        data = tuple([EVAL(x, env) for x in ast.val])
        return _MalData("LIST", data)
    else:
        return ast


if __name__=='__main__':     
    while True:
        try:
            x = input('user> ')
            rep(x)
            
        except Exception as e:
            print("".join(traceback.format_exception(*sys.exc_info())))
        except KeyboardInterrupt:
            pass

