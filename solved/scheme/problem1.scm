#lang scheme
(define (is-multiple-of-3-or-5 x) 
  (if (or (= (modulo x 5) 0)(= (modulo x 3) 0)) true false)
  )

(define (sum-of-multiples x)
  (cond ((<= x 0) 0)
        ((is-multiple-of-3-or-5 x) (+ x (sum-of-multiples (- x 1))))
        ( else (sum-of-multiples (- x 1)))
        )
  )

(sum-of-multiples 999)