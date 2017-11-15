;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname estructuras) (read-case-sensitive #t) (teachpacks ((lib "show-queen.ss" "teachpack" "htdp") (lib "image.ss" "teachpack" "2htdp") (lib "universe.ss" "teachpack" "2htdp") (lib "batch-io.ss" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "show-queen.ss" "teachpack" "htdp") (lib "image.ss" "teachpack" "2htdp") (lib "universe.ss" "teachpack" "2htdp") (lib "batch-io.ss" "teachpack" "2htdp")) #f)))
(require 2htdp/image)
;Racket incluye estructuras de datos:

;Un color se compone de
; red   - valor para el color rojo entre 0 y 255
; green - valor para el color verde entre 0 y 255
; blue  - valor para el color azul entre 0 y 255
(define color1 (make-color 255 155 10))
(circle 50 "solid" "red")
(circle 50 "solid" color1)
(add-line (empty-scene 160 90) 10 10 50 90 color1)

;Un posn se compone de
; x - valor de la componente en la dirección x
; y - valor de la componente en la dirección y
(define posn1 (make-posn 10 10))
(define posn2 (make-posn 50 90))
(add-line (empty-scene 160 90)
          (posn-x posn1) (posn-y posn1)
          (posn-x posn2) (posn-y posn2) "green")

(define posn3 (make-posn "Hola" 'mundo)) ;Problema?

;Para definir estructuras propias
;(define-struct est (el1 ... elN))
;(define (func-est e)
;        ... (est-el1 e) ...
;        ... (est-elN e) ...)

;Una est se compone de:
; el1 - primer elemento de la est
; el2 - segundo elemento de la est
;(define (func-est e)
;        ... (est-el1 e) ...
;        ... (est-el2 e) ...)
(define-struct est (el1 el2))

;Al definirla se tiene disponible un "constructor":
(make-est "e1" "e2")
;Un predicado para verificar el tipo:
(est? (make-est "e1" "e2"))
;Y selectores para los elementos:
(est-el1 (make-est "e1" "e2"))
(est-el2 (make-est "e1" "e2"))

;un registro se compone de:
; nombre -> string
; edad -> número
; genero -> symbol
(define-struct registro (nombre edad genero))
;func-registro: registro -> ?
;(define (func-registro r)
;   ... (registro-nombre r) ...
;   ... (registro-edad r) ...
;   ... (registro-genero r) ...)
;(make-registro 1 2 3)
(define r1 (make-registro "jp" 25 'h))
(define r2 (make-registro "jl" 23 'h))
(define r3 (make-registro "lp" 21 'm))
(define r4 (make-registro "ll" 20 'm))

;registro->lista
;Consume un registro
;Produce una lista con los elementos del registro
(check-expect (registro->lista r1) (list "jp" 25 'h))

(define (registro->lista r)
   (cons (registro-nombre r)
         (cons (registro-edad r)
               (cons (registro-genero r) empty))))

(define ldr (list r1 r2 r3 r4))

;Tarea:
;1
;draw-lineas
;Consume una lista de posn ldp una imagen y un color
;Produce las líneas que unen a los posn de ldp en color sobre la imagen

;2.a
;suma-edades
;Consume una lista de registros ldr
;Produce la suma de las edades de los registros de ldr
(check-expect (suma-edades ldr) 89)
(define (suma-edades l)
  (cond [(empty? l) 0]
        [(cons? l) (+ (registro-edad (first l))
                      (suma-edades (rest l)))]
        [else 'error]))

;2.b
;prom-edades
;Consume una lista de registros ldr
;Produce el promedio de las edades de los registros de ldr

