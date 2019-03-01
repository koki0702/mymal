import sys, traceback
import reader, printer
from maldata import _MalData
from env import Env
import core



repl_env = Env()

for key, val in core.ns.items():
    repl_env.set(key, val)



def READ(txt):
    ast = reader.read_str(txt)
    return ast


def EVAL(ast, env):
    if ast.type != "LIST":
        return eval_ast(ast, env)
    elif len(ast.val) == 0:
        return ast

    ast0 = ast.val[0]

    # def!
    if ast0.val == "def!":
        key = ast.val[1].val
        v = EVAL(ast.val[2], env)
        env.set(key, v)
        return v
    # let*
    elif ast0.val == "let*":
        let_env = Env(env)
        bidings = ast.val[1]

        for a, b in zip(bidings.val[0::2], bidings.val[1::2]):
            key = a.val
            v = EVAL(b, let_env)
            let_env.set(key, v)

        return EVAL(ast.val[2], let_env)
    # do
    elif ast0.val == "do":
        new_ast = eval_ast(_MalData("LIST", ast.val[1:]), env)
        return new_ast.val[-1]
    # if
    elif ast0.val == "if":
        b = EVAL(ast.val[1], env)
        if b.type != "NIL" and b.type != "FALSE":
            return EVAL(ast.val[2], env)
        else:
            if len(ast.val) <= 3: return _MalData("NIL")
            return EVAL(ast.val[3], env)
    # fn*
    elif ast0.val == "fn*":
        params = [p.val for p in ast.val[1].val]
        expr_ast = ast.val[2]

        def fn(*args):
            new_env = Env(env, params, args)
            return EVAL(expr_ast, new_env)
        return _MalData("FUNCTION", fn)

    # apply
    else:
        new_ast = eval_ast(ast, env)
        l = new_ast.val
        f, args = l[0].val, l[1:]
        return f(*args)


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

def PRINT(ast):
    txt = printer.pr_str(ast)
    return txt


def rep(x, env=repl_env):
    x = READ(x)
    x = EVAL(x, env)
    x = PRINT(x)
    print(x)
    return x




rep("(def! not (fn* (a) (if a false true)))")


if __name__=='__main__':

    #rep("(def! not (fn* (a) (if a false true)))")

    while True:
        try:
            x = input('user> ')
            rep(x, repl_env)
            
        except Exception as e:
            print("".join(traceback.format_exception(*sys.exc_info())))
        except KeyboardInterrupt:
            pass
