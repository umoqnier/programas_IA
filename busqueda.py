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


class Nodo:
    def __init__(self, nombre, actual=False, peso_acumulado=float('inf')):
        self.nombre = nombre
        self.actual = actual
        self.visitado = False
        self.peso_acumulado = peso_acumulado
        self.antecesor = None

    def __str__(self):
        return "Nodo " + self.nombre


class Grafo:
    def __init__(self):
        self.relaciones = {}

    def __str__(self):
        string_rep = "===Relaciones==="
        for node, value in zip(self.relaciones.keys(), self.relaciones.values()):  # TODO: optimizar for anidados
            string_rep = string_rep + "\nNODE " + node.nombre + " :"
            for rel in self.relaciones[node]:
                for subnode, peso in zip(rel.keys(), rel.values()):
                    string_rep = string_rep + "\n\t " + str(peso) + " -> " + subnode.nombre

        return string_rep

    def agrega_nodos(self, nodos):
        [self.relaciones.update({n: []}) for n in nodos]

    def crea_relacion(self, n_1, n_2, peso):
        self.relaciones[n_1].append({n_2: peso})

    def get_nodes(self):
        return self.relaciones.keys()

    def config(self):
        n_a = Nodo("A", True, 0)
        n_b = Nodo("B")
        n_c = Nodo("C")
        n_f = Nodo("F")
        n_d = Nodo("D")
        n_e = Nodo("E")
        self.agrega_nodos([n_a, n_b, n_c, n_f, n_d, n_e])
        self.crea_relacion(n_a, n_b, 7)
        self.crea_relacion(n_a, n_c, 9)
        self.crea_relacion(n_a, n_f, 14)
        self.crea_relacion(n_b, n_a, 7)
        self.crea_relacion(n_b, n_c, 10)
        self.crea_relacion(n_b, n_d, 15)
        self.crea_relacion(n_c, n_a, 9)
        self.crea_relacion(n_c, n_b, 10)
        self.crea_relacion(n_c, n_d, 11)
        self.crea_relacion(n_c, n_f, 2)
        self.crea_relacion(n_d, n_b, 15)
        self.crea_relacion(n_d, n_c, 11)
        self.crea_relacion(n_d, n_e, 6)
        self.crea_relacion(n_e, n_d, 6)
        self.crea_relacion(n_e, n_f, 9)
        self.crea_relacion(n_f, n_a, 14)
        self.crea_relacion(n_f, n_c, 2)
        self.crea_relacion(n_f, n_e, 9)

    def get_actual_node(self):
        for node in self.get_nodes():
            if node.actual:
                return node


def selecciona_menor_peso(caminos):
    aux = float('inf')
    s_node = None
    for camino in caminos:
        for sub_n in camino.keys():
            peso = camino[sub_n]
            if peso < aux:
                aux = peso
                s_node = sub_n
    return s_node, aux


def delete_visits(r):
    for relacion in r:
        for nodo, peso in zip(relacion.keys(), relacion.values()):
            if nodo.visitado:
                r.pop(r.index({nodo: peso}))
    return r


def dikstra(g):
    aux = list()
    g_relaciones = g.relaciones
    while g_relaciones:
        nodo_actual = g.get_actual_node()
        relaciones = g.relaciones[nodo_actual][:]  # Lista de relaciones del nodo actual
        relaciones = delete_visits(relaciones)
        while relaciones:
            nodo_m, peso = selecciona_menor_peso(relaciones)
            nodo_m.peso_acumulado = peso
            nodo_m.antecesor = nodo_actual
            aux.append(relaciones.pop(relaciones.index({nodo_m: peso})))
        nodo_n, _ = selecciona_menor_peso(aux)
        nodo_actual.visitado = True
        nodo_actual.actual = False
        nodo_n.actual = True


def a_star(g):
    pass


def bellman_ford(g):
    pass


def main():
    g = Grafo()
    g.config()
    dikstra(g)
    bellman_ford(g)
    a_star(g)


if __name__ == '__main__':
    main()
