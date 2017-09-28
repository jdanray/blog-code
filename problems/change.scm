;; count the number of ways to make change for a given amount
;; it's equal to the number of ways using the first denomination,
;; plus the number of ways without using the first denomination
(define (change amount denoms)
  (cond ((= amount 0)   1)
        ((< amount 0)   0)
        ((null? denoms) 0)
        (else           (+ (change (- amount 
                                      (car denoms))
                                   denoms)
                           (change amount
                                   (cdr denoms))))))

(print (change 100 '(50 25 10 5 1))) ;; 292
