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
    mensaje_cifrado = []
    banco = {"F": "A", "G": "B", "H": "C", "I": "D", "J": "D", "K": "E", "L": "A", "M": "B", "N": "C",
                       "O": "D", "P": "E", "Q": "A", "R": "B", "S": "C", "T": "D", "U": "E", "V": "A", "W": "B",
                       "X": "C", "Y": "D", "Z": "E"}
    for letra in letras:
        if letra == "A" or letra == "B" or letra == "C" or letra == "D" or letra == "E":
            mensaje_cifrado.append("A" + letra)
        elif letra == "F" or letra == "G" or letra == "H" or letra == "H" or letra == "I" or letra == "J" or letra == "K":
            mensaje_cifrado.append("B" + banco[letra])
        elif letra == "L" or letra == "M" or letra == "N" or letra == "O" or letra == "P":
            mensaje_cifrado.append("C" + banco[letra])
        elif letra == "Q" or letra == "R" or letra == "S" or letra == "T" or letra == "U":
            mensaje_cifrado.append("D" + banco[letra])
        elif letra == "V" or letra == "W" or letra == "X" or letra == "Y" or letra == "Z":
            mensaje_cifrado.append("E" + banco[letra])
    return "".join(mensaje_cifrado)


def codifica(mensaje):
    mensaje = mensaje.replace(" ", "").upper()
    return tabla(mensaje)


def decodifica(mensaje):
    i = 0
    nuevo = []
    indexes = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
    banco = {"A": ['A', 'B', 'C', 'D', 'E'], "B": ['F', 'G', 'H', 'IJ', 'K'], "C": ['L', 'M', 'N', 'O', 'P'],
             "D": ['Q', 'R', 'S', 'T', 'U'], "E": ['V', 'W', 'X', 'Y', 'Z']}

    while i < len(mensaje) - 1:
        sub = mensaje[i:i+2]
        aux = banco[sub[0]]
        nuevo.append(aux[indexes[sub[1]]])
        i += 2
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