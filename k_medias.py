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
from random import sample
from math import sqrt


def k_medias(k):
    """ Clasificador por K-medias """
    bandera = k - 1
    muestras = [[8, 10], [3, 10.5], [7, 13.5], [5, 18], [5, 13],
                [6, 9], [9, 11], [3, 18], [8.5, 12], [8, 16]]
    aux_muestras = muestras[:]
    medias_iniciales = [muestras[i] for i in sample(range(0, len(muestras)), k)]
    nuevas_medias = []
    pre_medias = []
    while medias_iniciales != nuevas_medias:
        conjunto_distancias = obtener_distancias(medias_iniciales, muestras)  # Lista de diccionarios {d: punto}
        c = formar_conjuntos(conjunto_distancias)


def obtener_distancias(medias, muestras):
    """ Funcion que obtiene las distancias entre las medias y el conjunto de muestras"""
    distancias = []
    conjunto_distancias = []
    for media in medias:
        for muestra in muestras:
            for i in range(len(media) - 1):  # Para vectores de n dimensiones
                d = sqrt(((muestra[i+1] - media[i+1])**2) + ((muestra[i] - media[i])**2))
                distancias.append({d: muestra})
        conjunto_distancias.append(distancias)
        distancias = []
    return conjunto_distancias


def formar_conjuntos(conjunto_d):
    """ Funcion que forma los conjuntos necesarios tomando la menor distancia """
    clasificaciones = []  # TODO: Crear lista con listas vacias. Tantas como clasifiaciones tengamos
    elements = []
    tam_dist = len(conjunto_d[0])  # Tamaño del conjunto de distancias
    for j in range(tam_dist):
        for i in range(len(conjunto_d)):
            elements.append(conjunto_d[i][j].keys())  # Se guarda la columna en una lista
        menor = min(elements)  # Obtiene el menor de la columna
        indice = elements.index(menor)  # Obtiene el indice para asignarlo a un conjunto
        elements = []
        clasificaciones.append(indice)  # Interesa el indice para obtener los vectores de la clasificacion

    return clasificaciones


def main():
    k = 2
    k_medias(k)


if __name__ == '__main__':
    main()
