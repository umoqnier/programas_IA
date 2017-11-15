%consult(ejemplo).

le_gusta(fulano, agua).
le_gusta(fulano, cerveza).
le_gusta(fulano, refresco).
le_gusta(fulano, leche).
le_gusta(zutano, cerveza).
le_gusta(zutano, refresco).
le_gusta(mengano, agua).
le_gusta(mengano, leche).

%Aritmetica

pertenece(X, Y, Z):- X>Y, X<Z.

suc(0, 1).
suc(X, Y):- X>0, Y is X+1.

n(c).
n(s(X)):- n(X).

suma(c, Y, Y):- n(Y).
suma(s(X), Y, s(Z)):- suma(X, Y, Z).

%suma(s(s(c)), s(c), s(s(s(c)))).
%suma(s(s(c)), s(c), Z).
%suma(s(c), Y, s(s(c))).
%suma(X, s(c), s(s(c))).

% Programa tarea ¿Cómo hacer una multiplicacion?
% a*0 = 0
% a*s(b) = a+(a*b)

%Version tipográfica
fact(0, s(0)).
fact(s(X), Y*s(X)):- fact(X, Y).

%Version numerica
fact2(0, 1).
fact2(X, Y):- X>0, X1 is X-1, fact2(X1, Y1), Y is X*Y1.

fib(0,s(0)).
fib(s(0),s(0)).
fib(s(s(X)),Y+Z):- fib(X,Y),fib(s(X),Z).

%LISTAS
%conc(A, B, C)
%conc([a, b], [b, c], C)
conc(A, B, C):- B=[], C=A.
conc(A, B, C):- B=[X|Y], conc(A, Y, D), C=[X|D].
conc2(A, B, C):- A=[], C=B.
conc2(A,B,C):- A=[X|Y], conc2(Y, B, D), C=[X|D].
conc3([],B,B).
conc3([X|Y], B, [X|D]):- conc3(Y, B, D).
