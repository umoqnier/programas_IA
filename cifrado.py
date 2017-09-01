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


def tabla(letras):
    """Funcion que se encarga de crear la tabla de codificacion"""
    mensaje_cifrado = []
    banco = {"F": 'A', "G": 'B', "H": 'C', "I": 'D', "J": 'D', "K": 'E', "L": 'A', "M": 'B', "N": 'C',
             "O": 'D', "P": 'E', "Q": 'A', "R": 'B', "S": 'C', "T": 'D', "U": 'E', "V": 'A', "W": 'B',
             "X": 'C', "Y": 'D', "Z": 'E'}  # Letra de cada fila relacionada con una letra columna
    for letra in letras:  # Se toma cada letra de la cadena
        if letra == "A" or letra == "B" or letra == "C" or letra == "D" or letra == "E":
            mensaje_cifrado.append("A" + letra)  # En el primer caso las letras fila concuerdan con las letras columna
        elif letra == "F" or letra == "G" or letra == "H" or letra == "H" or letra == "I" or letra == "J" or letra == "K":
            mensaje_cifrado.append("B" + banco[letra])
        elif letra == "L" or letra == "M" or letra == "N" or letra == "O" or letra == "P":
            mensaje_cifrado.append("C" + banco[letra])
        elif letra == "Q" or letra == "R" or letra == "S" or letra == "T" or letra == "U":
            mensaje_cifrado.append("D" + banco[letra])
        elif letra == "V" or letra == "W" or letra == "X" or letra == "Y" or letra == "Z":
            mensaje_cifrado.append("E" + banco[letra])
    return "".join(mensaje_cifrado)  # Se usa .join para sacar de la lista cada letras y convertir a cadena


def codifica(mensaje):
    """Funcion que se encarga de codificar un mensaje, depende de la funcion 'tabla'"""
    mensaje = mensaje.replace(" ", "").upper()  # Normalización de la cadena
    return tabla(mensaje)


def decodifica(mensaje):
    """Funcion encargada de decodificar un mensaje previamente codificado"""
    i = 0
    nuevo = []
    indexes = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}  # Cada letra corresponde a un indice de letra columna
    banco = {"A": ['A', 'B', 'C', 'D', 'E'], "B": ['F', 'G', 'H', 'IJ', 'K'], "C": ['L', 'M', 'N', 'O', 'P'],
             "D": ['Q', 'R', 'S', 'T', 'U'], "E": ['V', 'W', 'X', 'Y', 'Z']}  # Se declaran letras fila asociadas a
    #  cinco posibles letras columna

    while i < len(mensaje) - 1:
        sub_str = mensaje[i:i + 2]  # Toma de dos en dos letras de la cadena a decodificar
        aux = banco[sub_str[0]]  # Toma la primer letra y la usa como llave del banco. aux es una lista de letras ahora
        nuevo.append(aux[indexes[sub_str[1]]])  # Obtiene un número de indexes y asi la letra real de las posibles
        i += 2  # Suma dos para obtener las siguientes dos letras de la cadena
    return "".join(nuevo)


def main():
    while True:
        try:
            print("\n============================== Cifrador/Descifrador ==============================\n"
                  "    \t1. Cifrar\n"
                  "    \t2. Descifrar\n"
                  "    \t0. Salir")
            opcion = int(input("-->\t"))
            if opcion == 1:
                mensaje = input("Mensaje >> ")
                print("CIFRADO: ", codifica(mensaje))
            elif opcion == 2:
                mensaje = input("Mensaje >> ")
                print("DESCIFRADO: ", decodifica(mensaje))
            elif opcion == 0:
                print("""\t\t\t\t\t\t\t\t____________________________________
                                Developed by 
                                -Almazán García Giovanni
                                -Barriga Martínez Diego Alberto
                                -Bustamante Carrera Manuel Alejandro
                                -Juárez Pascual Karla Vanessa                    
                                -------------------------------------
                                \   ^__^
                                 \  (oo)\_______
                                    (__)\       )\/
                                        ||----w |
                                        ||     ||""")
                break
        except ValueError:
            print("\n\t== Ingrese solo valores numericos ==")


if __name__ == '__main__':
    main()
