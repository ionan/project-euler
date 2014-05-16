#lang scheme
(#%require "utils.scm")

(define (sum-of-squares x) (if (null? x) 0 (+ (square (car x)) (sum-of-squares (cdr x)))))

(define (square-of-sum x) (square (sum x)))

(define (sum-square-difference upper-bound)
        (define my-list (range 1 upper-bound))
        (- (square-of-sum my-list) (sum-of-squares my-list)))

(define (sum-square-difference-2 upper-bound) (- (square (sum-range upper-bound)) (sum-square-range upper-bound)))

(sum-square-difference-2 100)