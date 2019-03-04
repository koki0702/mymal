import sys, traceback
import reader, printer
from maldata import _MalData
from env import Env
import core



repl_env = Env()


def is_pair(ast):
    #if isinstance(ast, tuple) and len(ast) > 0: return True
    if ast.type == "LIST" or ast.type == "VECTOR":
        if len(ast.val) > 0: return True
    return False


def READ(txt):
    ast = reader.read_str(txt)
    return ast


def quasiquote(ast):

    if not is_pair(ast):
        _v = (_MalData("SYMBOLE", "quote"), ast)
        return _MalData("LIST", _v)
    elif ast.val[0].val == 'unquote':
        return ast.val[1]
    elif is_pair(ast.val[0]) and ast.val[0].val[0].val == 'splice-unquote':
        _v = (_MalData("SYMBOL", "concat"),
              ast.val[0].val[1],
              quasiquote(_MalData("LIST", ast.val[1:])))
        return _MalData("LIST", _v)
    else:
        _v = (_MalData("SYMBOL", "cons"),
              quasiquote(ast.val[0]),
              quasiquote(_MalData("LIST", ast.val[1:])))
        return _MalData("LIST",_v)


def EVAL(ast, env):
    while True:

        if ast.type != "LIST":
            return eval_ast(ast, env)

        if len(ast.val) == 0:
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
            a1, a2 = ast.val[1], ast.val[2]
            let_env = Env(env)

            for i in range(0, len(a1.val), 2):
                let_env.set(a1.val[i], EVAL(a1.val[i + 1], let_env))
            ast = a2
            env = let_env
        # do
        elif ast0.val == "do":
            eval_ast(_MalData("LIST", ast.val[1:-1]), env)
            ast = ast.val[-1]
        # if
        elif ast0.val == "if":
            b = EVAL(ast.val[1], env)
            if b.type != "NIL" and b.type != "FALSE":
                ast = ast.val[2]
            else:
                if len(ast.val) <= 3: ast = None
                ast = ast.val[3]
        # fn*
        elif ast0.val == "fn*":
            params = [p.val for p in ast.val[1].val]
            expr_ast = ast.val[2]

            def fn(*args):
                new_env = Env(env, params, args)
                return EVAL(expr_ast, new_env)
            fn.__ast__ = expr_ast
            fn.__gen_env__ = lambda args: Env(env, params, args)
            return _MalData("FUNCTION", fn)

        # quote
        elif ast0.val == "quote":
            return ast.val[1]
        elif ast0.val == "quasiquote":
            ast = quasiquote(ast.val[1])
        # apply
        else:
            new_ast = eval_ast(ast, env)
            l = new_ast.val
            f, args = l[0].val, l[1:]
            if hasattr(f, '__ast__'):
                ast = f.__ast__
                env = f.__gen_env__(args)
            else:
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


def rep(x, env=repl_env, out_print=True):
    x = READ(x)
    x = EVAL(x, env)
    x = PRINT(x)
    if out_print: print(x)
    return x



for key, val in core.ns.items():
    repl_env.set(key, val)

repl_env.set('eval', core._F(lambda ast: EVAL(ast, repl_env)))


rep("(def! not (fn* (a) (if a false true)))", out_print=False)
rep("(def! load-file (fn* (f) (eval (read-string (str \"(do \" (slurp f) \")\")))))", out_print=False)


if __name__=='__main__':
    _args = sys.argv[2:]
    repl_env.set('*ARGV*', _MalData('LIST', list(_args)))

    #rep("(def! not (fn* (a) (if a false true)))")
    if len(sys.argv) >= 2:
        path = sys.argv[1]
        rep('(load-file "' + path + '")')
        sys.exit(0)


    while True:
        try:
            x = input('user> ')
            rep(x, repl_env)

        except Exception as e:
            print("".join(traceback.format_exception(*sys.exc_info())))
        except KeyboardInterrupt:
            break
