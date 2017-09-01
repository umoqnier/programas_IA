#!/usr/bin/python
# -*- coding: utf-8 -*-
# Universidad Nacional Autonoma de Mexico / Facultad de Ingenieria
# Inteligencia Artificial
# Alumnos:
# Almazán García Giovanni
# Barriga Martínez Diego Alberto
# Bustamante Carrera Manuel Alejandro
# Juárez Pascual Karla Vanessa
# Hecho en Python 3.3

import os

def cls():  # Funcion para limpiar pantalla en cualquier S.O.
    if os.name == 'ce' or 'nt' or 'dos':
        os.system("cls")
    else:
        os.system("clear")

def encript(message):
	codedMessage = ""
	for i in message:
		codedMessage += encriptionKey[i]
	return codedMessage


def decript(encriptedMessage):
	words = encriptedMessage.split(" ")
	decodedMessage = ""
	for i in words:
		for j in range(0, len(i), 2):
			temp = i[j] + i[j + 1]
			decodedMessage += decriptionKey[temp]
		decodedMessage += " "
	return decodedMessage

while True:
	try:
		encriptionKey = {"a" : "AA", "b" : "AB", "c" : "AC", "d" : "AD", "e" : "AE",
						 "f" : "BA", "g" : "BB", "h" : "BC", "i" : "BD", "j" : "BD", "k" : "BE",
						 "l" : "CA", "m" : "CB", "n" : "CC", "o" : "CD", "p" : "CE",
						 "q" : "DA", "r" : "DB", "s" : "DC", "t" : "DD", "u" : "DE",
						 "v" : "EA", "w" : "EB", "x" : "EC", "y" : "ED", "z" : "EE", " ": " "}

		decriptionKey = {"AA" : "a", "AB" : "b", "AC" : "c", "AD" : "d", "AE" : "e",
						 "BA" : "f", "BB" : "g", "BC" : "h", "BD" : "i", "BD" : "j", "BE" : "k",
						 "CA" : "l", "CB" : "m", "CC" : "n", "CD" : "o", "CE" : "p",
						 "DA" : "q", "DB" : "r", "DC" : "s", "DD" : "t", "DE" : "u",
						 "EA" : "v", "EB" : "w", "EC" : "x", "ED" : "y", "EE" : "z", " ": " "}

		print("\n============================== Cifrador/Descifrador ==============================\n"
		                  "    \t1. Cifrar\n"
		                  "    \t2. Descifrar\n"
		                  "    \t0. Salir")
		option = int(input("Que desea hacer? ->\t"))

		if option == 1:
			cls()
			print("\n============================== Cifrado ==============================\n"
					"\t1. Leer del teclado\n"
					"\t2. Leer de un archivo .txt")
			choice = int(input("->\t"))
			if choice == 1:
				text = str(input("Ingrese el texto a codificar:\n->\t"))
				text = text.lower()
				print("\tMensaje cifrado:\n" + encript(text))
			elif choice == 2:
				name = str(input("Ingrese el nombre del archvivo con su extension\n->\t"))
				text = open(name, "r")
				result = open("codificado.txt", "w")
				for line in text:
					temp = line[0 : (len(line) - 1)]
					result.write(encript(temp) + "\n") # Esta linea solo se ocupa en caso de leer el texto de un archivo
				text.close()
				result.close()
				print("============================== Proceso finalizado ==============================\n")
				result = open("codificado.txt", "r")
				for line in result:
					print(line)
				result.close()
				print("\n============================== El mensaje codificado se guardo en el archivo codificado.txt ==============================")
		elif option == 2:
			cls()
			print("\n============================== Descifrado ==============================\n"
					"\t1. Leer del teclado\n"
					"\t2. Leer de un archivo .txt")
			choice = int(input("->\t"))
			if choice == 1:
				text = str(input("Ingrese el texto a decodificar:\n->\t"))
				text = text.upper()
				print("\tMensaje cifrado:\n" + decript(text))
			elif choice == 2:	
				name = str(input("Ingrese el nombre del archvivo con su extension\n->\t"))
				text = open(name, "r")
				result = open("decodificado.txt", "w")
				for line in text:
					temp = line[0 : (len(line) - 1)]
					result.write(decript(temp) + "\n")
				text.close()
				result.close()
				print("============================== Proceso finalizado ==============================\n")
				result = open("test.txt", "r")
				for line in result:
					print(line)
				result.close()
				print("\n============================== El mensaje decodificado se guardo en el archivo decodificado.txt ==============================")
		elif option == 0:
			print("""\t\t\t\t\t____________________________________
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
		else:
			print("\n\t== Opcion invalida, intente de nuevo ==")
	except ValueError:
		print("\n\t== Ingrese solo valores numericos ==")
	except KeyError:
		print("\n\t== Asegurese de no ingresar caracteres especiales ==")
