import sys
import reader, printer


repl_env = {'+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: int(a/b)}



def READ(txt):
	ast = reader.read_str(txt)
	return ast

def EVAL(ast):
	return ast

def PRINT(ast):
	txt = printer.pr_str(ast)
	return txt

def rep(x):
	x = READ(x)
	x = EVAL(x)
	x = PRINT(x)
	print(x)
	return x


def eval_ast(ast, env):
	if ast.type == "SYMBOL":
		key = ast.val
		if not key in env:
			raise Exception('no key for env')
		return env[key]
	elif isinstance(ast, tuple):
		return tuple([eval_ast(x, env) for x in ast])
	else:
		return ast


try:
	while True:
#		print("", end='')
		#print('>', end='')
		#sys.stdout.flush()
		#x = sys.stdin.readline()
		x = input('user> ')
		rep(x)

except KeyboardInterrupt:
	pass