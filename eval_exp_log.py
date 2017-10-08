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
from string import ascii_letters


def eval_rec(pa, fp=""):
    data = fp.split()
    operators = ["|", "&", "=>", "<=>", "!"]
    aux = data.pop(0)

    if aux in ascii_letters:  # Si se trata de una variable
        return pa[aux]  # retorno del valor de la variable diccionario[valor]
    elif aux in operators:  # Si no es una letra busca en los operadores
        val_1 = data.pop(0)  # Al menos se necesitará una variable (operadores unarios), opcional dos (operadores binarios)
        if aux == "&":
            val_2 = data.pop(0)
            return eval_rec(pa, val_1) and eval_rec(pa, val_2)
        elif aux == "|":
            val_2 = data.pop(0)
            return eval_rec(pa, val_1) or eval_rec(pa, val_2)
        elif aux == "!":
            return not eval_rec(pa, val_1)
        elif aux == "=>":
            val_2 = data.pop(0)
            return not eval_rec(pa, val_1) or eval_rec(pa, val_2)
        elif aux == "<=>":
            val_2 = data.pop(0)
            return (not eval_rec(pa, val_1) or eval_rec(pa, val_2)) and (not eval_rec(pa, val_1) or eval_rec(pa, val_2))
    else:
        fp = " ".join(data)
        return eval_rec(pa, fp)


def tdd(f, pa, fp, r):
    return f(pa, fp) == r


def main():
    print("  +++++ TDD +++++ ")
    # tdd(evP, fp, e, r)
    print(tdd(eval_rec, {"p": False, "q": False}, '( | p q )', False))
    print(tdd(eval_rec, {"p": True, "q": True}, '( & p q )', True))
    print(tdd(eval_rec, {"p": True, "q": False}, '( | p q )', True))
    print(tdd(eval_rec, {"p": True}, '( ! p )', False))
    print(tdd(eval_rec, {"p": True, "q": False}, '( => p q )', False))


if __name__ == '__main__':
    main()
