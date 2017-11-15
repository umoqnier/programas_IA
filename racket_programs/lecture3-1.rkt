;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname lecture3-1) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
;suma
;recibe: un número n
;produce: la suma de los n primeros naturales
;         'error si n es negativo
(check-expect (suma 5) 15)
(check-expect (suma 0) 0)
(check-expect (suma -1) 'error)
(define (suma n)
  (cond [(< n 0) 'error]
        [(zero? n) 0]
        [else (+ n (suma (sub1 n)))]))