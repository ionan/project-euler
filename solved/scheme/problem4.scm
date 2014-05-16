#lang scheme
(#%require "utils.scm")

(define (largest-product) 
        (define (_largest-product-iter1 x) (cond ((< x _min) -1) (else (max (_largest-product-iter2 x x) (_largest-product-iter1 (- x 1)))))) 
        (define (_largest-product-iter2 x y) (cond ((< y _min) -1) ((is-palindrome? (* x y)) (max (* x y) (_largest-product-iter2 x (- y 1)))) (else (_largest-product-iter2 x (- y 1))))) 
        (_largest-product-iter1 _max))

(define _max 999)
(define _min 100)
(largest-product)