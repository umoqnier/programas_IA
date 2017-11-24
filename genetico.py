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
import random

def gen_unidimensional(muestra):
    # Se hace un barrido para copiar la lista original elemento a elemento
    aux = muestra[:]
    print("".join(muestra))
    for j in range(100):
        i = 0
        while i < len(muestra) - 1:
            # Se verifica si la celula esta rodeada o si tiene lugar para reproducirse
            if muestra[i] == "*" and (muestra[i - 1] == "*" and muestra[i + 1] == "*"):
                aux[i] = " "
            elif muestra[i - 1] == "*" or muestra[i + 1] == "*":
                aux[i] = "*"
            i += 1
        # Se concatenan los elementos de la lista en una sola cadena para imprimirla
        print("".join(aux))
        muestra = aux[:]

while True:
    try:
        generacion = [" "] * 101
        print("\n============================== Automata celular ==============================\n"
                      "    \t1. Sierpinsky\n"
                      "    \t2. Muestra aleatoria\n"
                      "    \t0. Salir")
        opcion = int(input("-->\t"))
        if opcion == 1:
            generacion[50] = "*"
            gen_unidimensional(generacion)
        elif opcion == 2:
            celulas = random.randint(1, 101)                # Genera un número aleatorio de celulas iniciales
            for i in range(celulas):
                generacion[random.randint(0, 100)] = "*"    # Coloca esas celulas en posiciones aleatorias
            gen_unidimensional(generacion)
        elif opcion == 0:
            print("""\t\t\t\t____________________________________
                Developed by 
                -Almazán García Giovanni
                -Barriga Martínez Diego Alberto
                -Bustamante Carrera Manuel Alejandro
                -Juárez Pascual Karla Vanessa
                            Team
                -------------------------------------
                \   ^__^
                 \  (oo)\_______
                    (__)\       )\/
                        ||----w |
                        ||     ||""")
            break
        else:
            print("\n\t== Opcion invalida, intente de nuevo ==")
    except ValueError:
        print("\n\t== Ingrese solo valores numericos ==")
