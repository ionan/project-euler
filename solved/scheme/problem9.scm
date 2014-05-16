#lang scheme
(#%require "utils.scm")

(define _a -1)
(define _b -1)
(define _c -1)

(define (pythagorean-triplet? a b c)(= (+ (square a) (square b)) (square c)))

(define (display-result)(display _a)(display '*)(display _b)(display '*)(display _c)(display '=)(display (* _a _b _c)))

(define (special-pythagorean-triplet perimeter)
        (define (special-pythagorean-triplet-loop-1 a) 
                (cond ((> a perimeter) #f) 
                      ((> (special-pythagorean-triplet-loop-2 a (+ a 1)) 0) #t)
                      (else (special-pythagorean-triplet-loop-1 (+ a 1)))))
        (define (special-pythagorean-triplet-loop-2 a b) 
                (define c (- perimeter a b))
                (cond ((> b perimeter) -1)
                      ((pythagorean-triplet? a b c) (set! _a a)(set! _b b)(set! _c c)(* a b c))
                      (else (special-pythagorean-triplet-loop-2 a (+ b 1)))))
        (special-pythagorean-triplet-loop-1 1) (display-result))

(start_timing)
(special-pythagorean-triplet 1000)
(end_timing)