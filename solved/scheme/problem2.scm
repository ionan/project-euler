#lang scheme
(define (isEven? x) (= (modulo x 2) 0))

(define (greaterOrEqual x y) (or (> x y) (= x y)))

(define (_sumOfFibonacci n-1 n  max condition?)
  (define current (+ n n-1))
  (if (greaterOrEqual current max) 0 (if (condition? current) (+ current (_sumOfFibonacci n current max condition?)) (_sumOfFibonacci n current max condition?)))
  )

(define (sumOfFibonacci max condition?) 
  (cond ((greaterOrEqual 1 max) 0)
        ((greaterOrEqual 2 max) (if (condition? 1) 1 0))
        (else (+ (if (condition? 1) 1 0) (if (condition? 2) 2 0) (_sumOfFibonacci 1 2 max condition?)))
  )
)

(sumOfFibonacci 4000000 isEven?)