#lang scheme
(#%require "utils.scm")

(define _min 1)
(define _max 20)

(define (evenly-divisible-by-all x)
        (define (evenly-divisible-iter x y) (if (> y _max) #t (and (= (remainder x y) 0) (evenly-divisible-iter x (+ y 1)))))
        (evenly-divisible-iter x _min))

(define (smallest-multiple condition?) 
        (define step (product (filter-list is-prime? (range _min _max))))
        (define (smallest-multiple-iter x) (if (condition? x) x (smallest-multiple-iter (+ x step)))) 
        (smallest-multiple-iter step))

(smallest-multiple evenly-divisible-by-all)