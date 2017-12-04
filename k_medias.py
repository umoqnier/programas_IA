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
    # ========General========
    # medias_iniciales = [muestras[i] for i in sample(range(0, len(muestras)), k)] ALEATORIAS

    # ========Ejercicio en clase========
    # muestras = [[8, 10], [3, 10.5], [7, 13.5], [5, 18], [5, 13],
    #            [6, 9], [9, 11], [3, 18], [8.5, 12], [8, 16]]
    # medias_iniciales = [[8, 10], [5, 13]]

    # ========Tarea========
    muestras = [[1, 12.5], [3, 10.5], [3, 12.5], [3, 14.5], [3, 18],
                [5, 18], [5, 16], [5, 14.5], [5, 13], [6, 9], [8, 10],
                [9, 11], [8.5, 12], [7, 13.5], [8, 16], [0.5, 10.5]]
    medias_iniciales = [[3, 14.5], [9, 11]]
    while True:
        conjunto_distancias = obtener_distancias(medias_iniciales, muestras)  # Lista de diccionarios {d: punto}
        puntos_clasificados = formar_conjuntos(conjunto_distancias, k)
        nuevas_medias = actualiza_medias(puntos_clasificados)
        if nuevas_medias != medias_iniciales:
            medias_iniciales = nuevas_medias[:]
        elif nuevas_medias == medias_iniciales:
            return medias_iniciales, puntos_clasificados


def obtener_distancias(medias, muestras):
    """ Funcion que obtiene las distancias entre las medias y el conjunto de muestras"""
    distancias = []
    conjunto_distancias = []
    for media in medias:
        for muestra in muestras:
            for i in range(len(media) - 1):  # Para vectores de n dimensiones
                d = (sqrt(((muestra[i+1] - media[i+1])**2) + ((muestra[i] - media[i])**2)))
                distancias.append({d: muestra})
        conjunto_distancias.append(distancias)
        distancias = []
    return conjunto_distancias


def formar_conjuntos(conjunto_d, k):
    """ Funcion que forma los conjuntos necesarios tomando la menor distancia """
    clasificaciones = crear_listas_vacias(k)
    elements = []
    tam_dist = len(conjunto_d[0])  # Tamaño del conjunto de distancias
    for j in range(tam_dist):
        for i in range(len(conjunto_d)):
            elements.append(list(conjunto_d[i][j].keys()).pop())  # Se guarda la columna en una lista
        menor = min(elements)  # Obtiene el menor de la columna
        indice = elements.index(menor)  # Obtiene el indice para asignarlo a un conjunto
        elements = []
        clasificaciones[indice].append(conjunto_d[indice][j].get(menor))

    return clasificaciones


def crear_listas_vacias(k):
    espacio = []
    while k != 0:
        espacio.append(list())
        k -= 1
    return espacio


def actualiza_medias(conjunto):
    """ Funcion que actualiza las medias """
    suma = 0
    coordenada = 0
    nuevas_medias = []
    media = []
    dimension = len(conjunto[0][0])  # Se asume que todos los puntos son de la misma dimension
    for puntos in conjunto:
        while dimension > coordenada:
            for punto in puntos:
                for i in range(coordenada, len(punto), 2):
                    suma += punto[i]

            prom = suma / len(puntos)
            media.append(prom)
            coordenada += 1
            suma = 0
        nuevas_medias.append(media)
        media = []
        coordenada = 0

    return nuevas_medias


def main():
    k = 2
    i = 0
    medias, conjuntos_clasificados = k_medias(k)
    print("Medias -->", medias)
    for puntos in conjuntos_clasificados:
        print("Conjunto:", i+1, "-->", puntos)
        i += 1


if __name__ == '__main__':
    main()
