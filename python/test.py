from step9_try import *


rep('(try* (abc 1 2) (catch* exc (prn "exc is:" exc)))')
#rep('(try* 123 (catch* e 456))')
#rep('(throw "err1")')
#rep('(first nil)')
#rep('(rest nil)')
#rep('(macroexpand (cond false 7 false 8 false 9))')
#rep('(cond true 7)')
#rep('cond')
#rep('(defmacro! unless (fn* (pred a b) `(if ~pred ~b ~a)))')
#rep('(unless false 7 8)')

#rep( '(defmacro! identity (fn* (x) x))')
#rep('(let* (a 123) (identity a))' )

#rep('(quasiquote 7)')
#rep('(quasiquote (1 2 3))')
#rep('(quasiquote (unquote 7))')
#rep('(quasiquote (1 (unquote lst)))')
#rep('(def! c (quote (1 "b" "d")))')
#rep('(quasiquote (1 (splice-unquote c) 3))')
'''
rep('(def! a 6)')
rep('a')
rep('(def! b (+ a 2))')
rep('(+ a b)')
rep('(let* (c 2) c)')
'''
#rep('(let* (p (+ 2 3) q (+ 2 p)) (+ p q))')



"""
rep('(fn* [a] a)')
rep('( (fn* [a] a) 7)')
rep('( (fn* [a] (+ 2 1)) 10)')
rep('( (fn* [a] (+ a 1)) 10)')
rep('( (fn* [a b] (+ a b)) 2 3)')
"""

"""
rep('(list? (list))')
rep('(empty? (list))')
rep('(empty? (list 1))')
rep('(count (list 1 2 3))')
rep('(count nil)')
#rep('(list 1 2 3)')
rep('(if (> (count (list 1 2 3)) 3) "yes" "no")')
rep('(if (>= (count (list 1 2 3)) 3) "yes" "no")')
rep('(if true 7 8)')
rep('(if false 7 8)')
"""

"""
rep('(= (list) nil)')
rep('(= 2 1)')
rep('(= 1 1)')
rep('(= 1 (+ 1 1))')
rep( '(= 2 (+ 1 1))')
rep('(= (list) (list))')
"""
#rep('(prn "hello koki")')
#rep('(do (prn "prn output1"))')
#rep( '(= (list 1 2) (list 1 2))')
#rep('( (fn* (& more) (count more)) 1 2 3)')
#rep('(not false)')
#rep('(pr-str)')
#rep('(pr-str "")')
#rep('(pr-str "abc")')
#rep('(pr-str "abc  def" "ghi jkl")')
#rep('(str "")')
#rep('(prn "abc  def" "ghi jkl")')
#rep('(= [] (list))')

#rep('(+ 1 2)')
#rep('(list + 1 2)')

"""
# できなかったテスト
rep('(= [(list)] (list []))')
print('------')
rep('[(list)]')
print('------')
rep('(list [])')
"""

"""
#rep('(str "ttt ttt")')
rep('(def! mal-prog (list + 1 2))')
rep('(eval mal-prog)')


rep('(slurp "../tests/incA.mal")')
rep('(load-file "../tests/incA.mal")')
rep('(inc4 3)')

rep('(def! a (atom 2))')

rep('(def! inc3 (fn* (a) (+ 3 a)))')
rep('(def! a (atom 2))')
rep('(swap! a inc3)')
"""

#rep(';;tt\n(def! inc4 (fn* (a) (+ 4 a)))')

#rep('(load-file "../tests/incB.mal")')
#rep('(read-string (str (slurp "../tests/incB.mal")))')