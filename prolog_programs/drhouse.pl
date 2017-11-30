% Hechos
tiene_sintoma(manuel, fiebre).
tiene_sintoma(alicia, cansancio).
sintoma_de(fiebre, gripe).
sintoma_de(tos, gripe).
sintoma_de(cansancio, anemia).
elimina(vitamina, cansancio).
elimina(aspirina, fiebre).
elimina(jarabe, tos).

% Reglas

receta_a(X, Y):- enfermo_de(Y, A), alivia(X, A).
alivia(X, Y):- elimina(X, A), sintoma_de(A, Y).
enfermo_de(X, Y):- tiene_sintoma(X, Z), sintoma_de(Z, Y).
