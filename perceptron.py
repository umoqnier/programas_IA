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

def perceptron(muestras, resultados, pesos, taza = 0.1):
    pesosPrev = []
    while pesosPrev != pesos:
        i = 0
        pesosPrev = pesos[:]
        for muestra in muestras:
            salida = 0
            temp = list(map(lambda x, y: x * y, pesos, muestra))
            for n in temp:
                salida += n
            delta = taza * (resultados[i] - g(salida))
            pesos = updatePesos(pesos, muestra, delta)
            i += 1
        print("\t\tPesos->\t", pesos)
    return pesos


def updatePesos(pesos, muestra, delta):
    n_pesos = []
    for m, p in zip(muestra, pesos):
        p = p + m * delta
        n_pesos.append(p)
    return n_pesos


def g(pulse):
    if pulse >= 0:      # Se define el umbral en 0
        return 1
    else:
        return -1


def main():
             # x0, x1, x2
    muestras = [[1, 0, 0],
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 1]]
    resultados = [-1, 1, 1, -1]
    taza = 0.1
    # Pesos iniciales igual a 0
    pesosInit = [0, 0, 0]

    pesosResult = perceptron(muestras, resultados, pesosInit, taza)
    print("\n\tPesos Finales:\t", pesosResult)


if __name__ == '__main__':
    main()
