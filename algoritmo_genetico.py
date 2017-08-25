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


def gen_unidimensional(simbolo, longitud, posicion):
    generacion = [""] * longitud
    generacion[posicion] = simbolo
    aux = generacion[:]
    print("\t".join(generacion))
    for j in range(15):
        i = 0
        while i < len(generacion)-1:
            if generacion[i] == simbolo and (generacion[i-1] == simbolo and generacion[i+1] == simbolo):
                aux[i] = ""
            elif generacion[i - 1] == simbolo or generacion[i + 1] == simbolo:
                aux[i] = simbolo
            i += 1
        print("\t".join(aux))
        generacion = aux[:]


gen_unidimensional("°", 41, 20)