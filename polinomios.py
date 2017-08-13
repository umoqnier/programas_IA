#!/usr/bin/python
# -*- coding: utf-8 -*-
# Universidad Nacional Autonoma de Mexico / Facultad de Ingenieria
# Lenguajes de programacion
# Alumnos:
# Barriga Martínez Diego Alberto
# Bustamante Carrera Manuel Alejandro
# Juárez Pascual Karla Vanessa
# Hecho en Python 3.6


def crea_polinomio():
    i = 0
    grado = int(input("Grado maximo>> "))
    aux = []
    while i <= grado:
        coeficiente = int(input(("Coeficiente x^" + str(i) + ": ")))
        aux.append(coeficiente)
        i = i + 1
    return aux


def valor_punto(polinomio):
    print("==============Valor calculado en un punto==============\n")
    punto = int(input("Punto>> "))
    z = 0
    potencias = []
    for j in range(0, len(polinomio)):
        potencias.insert(j, pow(punto, z))
        z += 1
    multiplicacion = 0

    for k in range(0, len(polinomio)):
        multiplicacion = multiplicacion + (polinomio[k] * potencias[k])
        k += 1
    print("Valor>> " + str(multiplicacion))


def operaciones(opcion):
    if opcion == 1:  # Valor en un punto
        polinomio = crea_polinomio()
        valor_punto(polinomio)
        return True
    elif opcion == 2:  # Suma
        pass
    elif opcion == 3:  # Resta
        pass
    elif opcion == 4:  # Multiplicacion
        pass
    elif opcion == 5:  # Derivada
        pass
    elif opcion == 6:  # Integral
        pass
    elif opcion == 0:
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
