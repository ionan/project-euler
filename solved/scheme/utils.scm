#lang scheme
(#%provide (all-defined))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;  LIST UTILS  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;Convert a number to a list of digits
(define (number->list x) (if (< x 10) (list x) (append (list (remainder x 10)) (number->list (quotient x 10)))))

;Reverse the given list
(define (reverse-list my-list) (if (null? my-list) '() (append (reverse-list (cdr my-list)) (list (car my-list)))))

;Remove first and last elements from the given list
(define (remove-first-and-last x) (reverse-list (cdr (reverse-list (cdr x)))))

;Returns the product of all elements in the list
(define (product x) (if (null? x) 1 (* (car x) (product (cdr x)))))

;Returns the sum of all elements in the list
(define (sum x) (if (null? x) 0 (+ (car x) (sum (cdr x)))))

;Returns a list with numbers from lower to upper
(define (range lower upper) (if (= lower upper) (list upper) (append (list lower) (range (+ lower 1) upper))))

;Filters the given list
(define (filter-list predicate? x) 
        (cond ((null? x) '())
              ((predicate? (car x)) (append (list (car x)) (filter-list predicate? (cdr x))))
              (else (filter-list predicate? (cdr x)))))

;Returns the length of a list
(define (length-list x) (if (null? x) 0 (+ 1 (length-list (cdr x)))))

;Takes the first n items of the list x
(define (take n l) 
        (define (take-iter n l) (if (= n 0) '() (append (list (car l)) (take-iter (- n 1) (cdr l)))))
        (if (< (length l) n) l (take-iter n l)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;  NUMBER UTILS  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;Sums values from 1 to the given upper limit using the formula: sum(n) = n*(n + 1)/2
(define (sum-range n)(/ (* n (+ n 1)) 2))

;Sums square values from 1 to the given upper limit using the formula:  n/6*(2n + 1)*(n + 1)
(define (sum-square-range n)(* (/ n 6) (+ (* 2 n) 1) (+ n 1)))

;Returns the square of the given number
(define (square x) (* x x))

;Returns the square root of the given number (As in SICP book)
(define (sqrt x)
  (define (sqrt-iter guess x) (if (good-enough? guess x) guess (sqrt-iter (improve guess x) x)))
  (define (improve guess x) (average guess (/ x guess)))
  (define (average x y) (/ (+ x y) 2))
  (define (good-enough? guess x) (< (abs (- (square guess) x)) 0.001))
  (sqrt-iter 1.0 x))

;Checks wether the given number is prime or not
(define (is-prime? x) 
        (define (is-prime-iter? x current upper) (if (> current upper) #t (and (> (remainder x current) 0) (is-prime-iter? x (+ current 2) upper))))
        (cond ((< x 4) #t)
              ((and (> (remainder x 2) 0) (> (remainder x 3) 0)) (is-prime-iter? x 5 (+ (sqrt x) 1)))
              (else #f)))

;Checks wether the given number is palindrome or not
(define (is-palindrome? x) (define (_is-palindrome? x) (if (or (null? x) (null? (cdr x))) #t (and (= (car x) (car (reverse-list x))) (_is-palindrome? (remove-first-and-last x))))) (_is-palindrome? (number->list x)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;  TIMING UTILS  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define _start (current-inexact-milliseconds))
(define (start_timing) (set! _start (current-inexact-milliseconds)))
(define (end_timing) (newline)(display (- (current-inexact-milliseconds) _start)))