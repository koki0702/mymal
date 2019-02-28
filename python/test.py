from step2_eval import *


x = '(* -3 6)'
#x = '(+ 2 (* 3 4))'
x = READ(x)
x = EVAL(x, repl_env)
print(PRINT(x))
