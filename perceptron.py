#!/usr/bin/python
# -*- coding: utf-8 -*-
# Universidad Nacional Autonoma de Mexico / Facultad de Ingenieria
# Inteligencia Artificial
# Alumnos:
# Almazán García Giovanni
# Barriga Martínez Diego Alberto
# Bustamante Carrera Manuel Alejandro
# Juárez Pascual Karla Vanessa
# Hecho en Python 3.5

from functools import reduce


def perceptron(muestras, resultados, pesos, taza=0.1):
    old_pesos = []

    while old_pesos != pesos:
        resultados_iter = iter(resultados)
        for muestra in muestras:
            salida = reduce((lambda x, y: x+y), [p * m for p, m in zip(pesos, muestra)])
            resultado = get_resultado_actual(resultados_iter)
            delta = taza * (resultado - g(salida))
            old_pesos = pesos[:]
            if delta != 0:
                pesos = actualiza_pesos(pesos, muestra, delta)
        print(pesos)
    return pesos


def get_resultado_actual(r):
    return next(r)


def actualiza_pesos(pesos, muestra, delta):
    n_pesos = []
    for m, p in zip(muestra, pesos):
        p = p + m*delta
        n_pesos.append(p)
    return n_pesos


def g(pulse):
    if pulse >= 0:
        return 1
    else:
        return -1


def main():
             # x0, x1, x2
    muestras = [[1, 0, 0],
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 1]]
    resultados = [1, 1, 1, -1]
    taza = 0.1
    pesos = [0, 0, 0]

    resultado = perceptron(muestras, resultados, pesos, taza)
    print("Final:", resultado)


if __name__ == '__main__':
    main()
