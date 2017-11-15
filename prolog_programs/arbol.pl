% Hechos
hombre(pedro).
hombre(paco).
hombre(luis).
hombre(diego).
mujer(luz).
mujer(maria).
mujer(luisa).
mujer(lola).
progenitor(lola, pedro).
progenitor(luis, pedro).
progenitor(luisa, luz).
progenitor(diego, luz).
progenitor(pedro, paco).
progenitor(pedro, maria).
progenitor(luz, paco).
progenitor(luz, maria).

% Reglas

madre(X, Y):- progenitor(X, Y), mujer(X).
padre(X, Y):- progenitor(X, Y), hombre(X).

hijo(X, Y):- progenitor(Y, X), hombre(X).
hija(X, Y):- progenitor(Y, X), mujer(X).

abuela(X, Y):- progenitor(X, Z), progenitor(Z, Y), mujer(X).
abuelo(X, Y):- progenitor(X, Z), progenitor(Z, Y), hombre(X).

% TAREA:- Definir Hermanos, tios y primos
