#lang scheme
(#%require "utils.scm")

(define (nth-prime n) 
        (define (nth-prime-iter n i x) (if (is-prime? x) (if (= n i) x (nth-prime-iter n (+ i 1) (+ x 2))) (nth-prime-iter n i (+ x 2))))
        (cond ((= n 1) 2)
              ((= n 2) 3)
              (else (nth-prime-iter n 3 5))))

(nth-prime 2000)
