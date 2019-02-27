import sys

def READ(x):
	return x

def EVAL(x):
	return x

def PRINT(x):
	print(x)
	return x

def rep(x):
	while True:
		x = READ()
		x = EVAL(x)
		PRINT(x)


while True:
	print("user>")
	x = sys.stdin.readline()
	rep(x)
