# 						Programa que realiza operaciones con vectores

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Universidad Nacional Autonoma de Mexico / Facultad de Ingenieria
# inteligenica Artificial
# Alumnos:
#	Barriga Martínez Diego Alberto
#	Bustamante Carrera Manuel Alejandro
#	Juárez Pascual Karla Vanessa
# Hecho en Python 3.3
import os
import math

def cls():					# Funcion para limpiar pantalla en cualquier S.O.
	if os.name == 'ce' or 'nt' or 'dos':
		os.system("cls")
	else:
		os.system("clear")

def creaVector():
	#dim = int(input("Ingresa de que dimension sera el vector -->\t"))
	v = input("\nIngrese las componentes del vector separadas por un espacio\n-->\t")
	v = v.split(" ")
	vector = list(map(lambda n: float(n), v))
	
	#print(vector)
	#print(type(vector))
	return vector

def suma():
	print("\n========= SUMA =========\n")
	num = int(input("Ingrese cuantos vectores desea sumar -->\t"))
	vectores = []
	total = []
	for i in range(0,num):
		vectores.append(creaVector())
	print(vectores)
	total = vectores[0]
	jump = True
	for i in vectores:
		if not jump:
			m = 0
			for j in i:
				total[m] += j
				m += 1
		jump = False 
	print("\n\t El resultado de la suma es: " + str(total))

def resta():
	print("\n========= RESTA =========\n")
	num = int(input("Ingrese cuantos vectores desea restar -->\t"))
	vectores = []
	total = []
	for i in range(0,num):
		vectores.append(creaVector())
	print(vectores)
	total = vectores[0]
	jump = True
	for i in vectores:
		if not jump:
			m = 0
			for j in i:
				total[m] -= j
				m += 1
		jump = False 
	print("\n\t El resultado de la resta es: " + str(total))

def producto():
	print("\n========= PRODUCTO =========")
	vector = creaVector()
	escalar = float(input("Ingrese el escalar que multiplicara al vector -->\t"))
	print("\n\t El producto es: " + str(list(map(lambda n: escalar * n, vector))))

def norma():
	print("\n========= NORMA =========")
	vector = creaVector()
	temp = list(map(lambda n: n ** 2, vector))
	temp1 = 0
	for i in temp:
		temp1 += i
	print("\n\t La norma es: " + math.sqrt(temp1))

while True:
	print("\n========= Programa encargado de hacer operaciones con vectores =========\n"
              "    \t1. Suma\n"
              "    \t2. Resta\n"
              "    \t3. Producto por escalar\n"
              "    \t4. Norma\n"
              "    \t5. Angulo entre dos vectores\n"
              "    \t0. Salir")
	opcion = int(input("-->\t"))
	if opcion:
		cls()
	if opcion == 1:		# Suma
		suma()
	elif opcion == 2:	# Resta
		resta()
	elif opcion == 3:	# Producto
		producto()
	elif opcion == 4:	# Norma
		norma()
	elif opcion == 5:	# Angulo
		pass
	elif opcion == 0:
		break
	else:
		print("\n\t\tOpcion invalida, intente de nuevo")
#creaVector()
