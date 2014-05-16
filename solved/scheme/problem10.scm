#lang scheme
(#%require "utils.scm")

(define (is-divisible-by-any x lst) 
        (if (null? lst) #f (or (= (remainder x (car lst)) 0) (is-divisible-by-any x (cdr lst)))))

(define (list-of-primes upper-bound)
        (define (get-next-odd x) (if (= (remainder x 2) 0) (+ x 1) (+ x 2)))
        (define (list-of-primes-iter current lst)
                (cond ((> current upper-bound) lst)
                      ((< current 2) '())
                      ((is-divisible-by-any current lst) (list-of-primes-iter (get-next-odd current) lst))
                      (else (list-of-primes-iter (get-next-odd current) (cons current lst)))))
         (list-of-primes-iter 2 '()))

(start_timing)
(list-of-primes 100000)
(end_timing)