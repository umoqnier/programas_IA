;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname prom_meno_l) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

(define (menores n)
  (cond [(zero? n) empty]
        [else (cons n (menores (sub1 n)))]
        ))

(define (suma l)
  (cond [(empty? l) 0] 
        [else (+ (first l) (suma (rest l)))]
        ))

(define (count l)
  (cond [(empty? l) 0]
        [else (+ 1 (count (rest l)))]
        ))

(define (prom l)
  (/ (suma l) (count l)))