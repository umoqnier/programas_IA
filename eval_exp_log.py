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
    letters = ascii_letters
    operators = ["|", "&", "=>", "<=>", "!"]
    aux = data.pop(0)
    if fp == "":
        return pa[aux]
    elif aux in operators:
        if aux == "&":
            return eval_rec(pa) and eval_rec(pa)
        elif aux == "|":
            return eval_rec(pa) or eval_rec(pa)
        elif aux == "!":
            return eval_rec(not pa[data.pop(0)])
        elif aux == "=>":
            return not eval_rec(pa) or eval_rec(pa)
        elif aux == "<=>":
            return (not eval_rec(pa) or eval_rec(pa)) and (not eval_rec(pa) or eval_rec(pa))
    else:
        fp = " ".join(data)
        eval_rec(pa, fp)


def tdd(f, fp, pa, r):
    return f(fp, pa) == r


def main():
    print("  +++++ TDD +++++ ")
    # tdd(evP, fp, e, r)
    print(tdd(eval_rec, {"p": True, "q": False}, '( | p q )', True))


if __name__ == '__main__':
    main()
