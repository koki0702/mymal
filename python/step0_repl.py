import sys

def READ(x):
    return x

def EVAL(x):
    return x

def PRINT(x):
    return x

def rep(x):
    x = READ(x)
    x = EVAL(x)
    x = PRINT(x)
    print(x)
    return x


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