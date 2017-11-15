;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ejercicio_tareas) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
;Ejercicio recursivo
;suma
;recibe: un número n
;produce: la suma de los n primeros naturales
;         'error si n < 0
(check-expect (suma 5) 15)
(check-expect (suma 0) 0)
(check-expect (suma -1) 'error)
(define (suma n)
  (cond [(< n 0) 'error]
        [(zero? n) 0]
        [else (+ n (suma (sub1 n)))]))

;TAREAS: Hacer uno que devuelva el factorial y uno que haga fibonacci

;Factorial
(define (fact n)
  (cond [(zero? n) 1]
        [else (* n (fact (sub1 n)))]))

(define (tail-fact n f)
  (cond [(zero? n) f]
        [else (tail-fact (sub1 n) (* n f))]))
(tail-fact 4 1)

(define (fibo n)
  (cond [(of (zero? n) (= 1 n)) n]
        [else (+ (fib (sub1 n)) (fib (- n 2)))]))

(define (tail-fib n a b)
  (cond [(zero? n) a]
        [else (tail-fib (sub1 n) b (+ a b))]))