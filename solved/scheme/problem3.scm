#lang scheme
(define (_get-primes x y) 
        (cond ((< x 2) '() )
              ((= (modulo x y) 0) (append (list y) (_get-primes (/ x y) 2)))
              (else (_get-primes x (+ y 1)))
        )
)

(define (get-primes x) (car (reverse (_get-primes x 2))))

(get-primes 600851475143)