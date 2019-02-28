import sys
import reader, printer


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