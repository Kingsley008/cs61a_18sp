(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car(cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car(cdr (cdr s)))
)

(define (sign x)
  'YOUR-CODE-HERE
  (cond ((< x 0) -1)
        ((> x 0) 1)
        (else 0)
    )
)

(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
  (cond  ((= n 1) b)
         ((even? n) (square (pow b (/ n 2))))
         ((odd? n) (* b (square (pow b (/ (- n 1) 2)))))
         (else 0)
    )
)

(define (ordered? s)
  'YOUR-CODE-HERE
  (cond
         ((null? (cdr s)) #t)
         ((< (car s) (car(cdr s))) (ordered? (cdr s)))
         ((> (car s) (car(cdr s))) #f)
         ((= (car s) (car(cdr s))) (ordered? (cdr s)))
          )
)

(define (nodots s)
  'YOUR-CODE-HERE
  (cond
        ((null? s) ())
        ((pair? s)
          (if(pair? (car s))
            (cons (nodots(car s)) (nodots(cdr s)))
            (cons (car s) (nodots(cdr s)))
            )
          )
        (else (cons s nil))
    )
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) #f)
          ((= (car s) v) #t)
          ((> (car s) v) #f)
          (else (contains?(cdr s) v))
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)v

(define (add s v)
    (cond ((empty? s) (list v))
          ((< v (car s) ) (cons v s))
          ((= (car s) v) (cons v (cdr s)))
          ((and (> v (car s)) (null? (cdr s))) (cons (car s)(cons v nil)))
          ((and (> v (car s)) (< v (car(cdr s)))) (cons (car s)(cons v (cdr s))))
          (else (cons (car s) (add (cdr s) v)))
          ))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((=(car s)(car t)) (cons (car s) (intersect (cdr s) (cdr t))))
          ((<(car s)(car t)) (intersect (cdr s) t))
          ((>(car s)(car t)) (intersect s (cdr t)))
          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s)(car t)) (cons (car s) (union (cdr s) (cdr t))))
          ((< (car s)(car t)) (cons (car s) (union(cdr s) t )))
          ((< (car t)(car s)) (cons (car t) (union s (cdr t))))
      ))