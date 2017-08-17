#!/usr/bin/python
# -*- coding: utf-8 -*-
# Universidad Nacional Autonoma de Mexico / Facultad de Ingenieria
# Inteligencia Artificial
# Alumnos:
# Almazán García Giovanni
# Barriga Martínez Diego Alberto
# Bustamante Carrera Manuel Alejandro
# Juárez Pascual Karla Vanessa
# Hecho en Python 3.5 y utilizando la biblioteca numpy

import numpy as np


def crea_polinomio():
    i = 0
    grado = int(input("Grado maximo>> "))
    aux = []
    while i <= grado:
        coeficiente = int(input(("Coeficiente x**" + str(i) + ": ")))
        aux.append(coeficiente)
        i = i + 1
    aux.reverse()
    return aux


def suma(polinomio_1, polinomio_2):
    p_1 = np.poly1d(polinomio_1)
    p_2 = np.poly1d(polinomio_2)
    return p_1 + p_2


def resta(polinomio_1, polinomio_2):
    p_1 = np.poly1d(polinomio_1)
    p_2 = np.poly1d(polinomio_2)
    return p_1 - p_2


def multiplicacion(polinomio_1, polinomio_2):
    p_1 = np.poly1d(polinomio_1)
    p_2 = np.poly1d(polinomio_2)
    return p_1 * p_2


def derivada(polinomio):
    p = np.poly1d(polinomio)
    return np.polyder(p)


def integral(polinomio):
    p = np.poly1d(polinomio)
    return np.polyint(p)


def valor_punto(polinomio, punto):
    p = np.poly1d(polinomio)
    return p(punto)


def operaciones(opcion):
    if opcion == 1:  # Valor en un punto
        print("==============Valor calculado en un punto==============\n")
        punto = int(input("Punto>> "))
        polinomio = crea_polinomio()
        print("VALOR>> ", valor_punto(polinomio, punto))
        return True
    elif opcion == 2:  # Suma
        print("==============Suma==============\n")
        print("Polinomio 1")
        polinomio_1 = crea_polinomio()
        print("Polinomio 2")
        polinomio_2 = crea_polinomio()
        print("SUMA>> ")
        print(suma(polinomio_1, polinomio_2))
        return True
    elif opcion == 3:  # Resta
        print("==============Resta==============\n")
        print("NOTA: Polinomio 1 - polinomio 2")
        print("Polinomio 1")
        polinomio_1 = crea_polinomio()
        print("Polinomio 2")
        polinomio_2 = crea_polinomio()
        print("RESTA>> ")
        print(resta(polinomio_1, polinomio_2))
        return True
    elif opcion == 4:  # Multiplicacion
        print("==============Multiplicación==============\n")
        print("Polinomio 1")
        polinomio_1 = crea_polinomio()
        print("Polinomio 2")
        polinomio_2 = crea_polinomio()
        print("MULTIPLICACION>> ")
        print(multiplicacion(polinomio_1, polinomio_2))
        return True
    elif opcion == 5:  # Derivada
        print("==============Derivada==============\n")
        polinomio = crea_polinomio()
        print("DERIVADA>> ")
        print(derivada(polinomio))
        return True
    elif opcion == 6:  # Integral
        print("==============Integral==============\n")
        polinomio = crea_polinomio()
        print("INTEGRAL>> ")
        print(integral(polinomio))
        return True
    elif opcion == 0:
        print("""\t\t\t\t____________________________________
                Developed by 
                -Almazán García Giovanni
                -Barriga Martínez Diego Alberto
                -Bustamante Carrera Manuel Alejandro
                -Juárez Pascual Karla VanessaTeam
                -------------------------------------
                \   ^__^
                 \  (oo)\_______
                    (__)\       )\/
                        ||----w |
                        ||     ||""")
        return False
    else:
        print("*Error* Intenta otra opcion *Error*")


def main():
    while True:
        print("\n"
              "----*Programa encargado de hacer operaciones entre polinomios*----\n"
              "    1-Valor calculado en un punto\n"
              "    2-Suma\n"
              "    3-Resta\n"
              "    4-Multiplicacion\n"
              "    5-Derivada\n"
              "    6-Integral\n"
              "    0-Salir"
              )
        opcion = int(input("# "))
        if not operaciones(opcion):
            break


if __name__ == '__main__':
    main()
