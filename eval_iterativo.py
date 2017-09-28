#!/usr/bin/python3
# EJERCICIO DE CLASE
# Programa que realiza la evaluación de expresiones lógicas de forma iterativa
# Dikstra Algorithm
# f ==> Funcion: evP
# fp ==> Funcion proposicional: '( p | q )'
# e ==> Evaluaciones: {q: True, p: False}
# r ==> Resultados: True or False


def evP(fp, e):
    data = fp.split()  # convertir a una lista la funcion proposicional
    dic_unari = {"!": 'not '}
    dic_binary = {"|": ' or ', "&": ' and ', "=>":''}
    S, V = [], []
    for d in data:
        if d == '(':
            pass
        elif d in dic_unari or d in dic_binary:
            S.append(d)
        elif d == ')':
            op, va = S.pop(), V.pop()
            if op in dic_unari:
                va = eval(dic_unari[op] + repr(va))
            elif op == '=>':
                va = not V.pop() or va
            else:
                va = eval(repr(V.pop()) + dic_binary[op] + repr(va))
            V.append(va)
        else:
            V.append(e[d])
    return V


def tdd(f, fp, e, r):
    return f(fp, e) == r


print("  +++++ TDD +++++ ")
# tdd(evP, fp, e, r)
print(tdd(evP, '( p | q )', {"p": True, "q": False}, [True]))
print(tdd(evP, '( p => q )', {"p": True, "q": False}, [False]))
print(tdd(evP, '( p => q )', {"p": True, "q": True}, [True]))
fp = '( ( ( p => q ) => ( ( p & r ) => ( q & r ) ) ) )'
print(fp)
for p in [False, True]:
    for q in [False, True]:
        for r in [False, True]:
            print(tdd(evP, fp, {"p": p, "q": q, "r": r}, [True]))
