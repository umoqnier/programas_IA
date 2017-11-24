def perceptron():
    pesos = [0, 0, 0]
    taza = 0.1
             # x0, x1, x2
    muestras = [[1, 0, 0], 
                [1, 0, 1], 
                [1, 1, 0], 
                [1, 1, 1]]

    resultados = iter([1, 1, 1, -1])
  
    for muestra in muestras:
        salida += [ p * m for p, m in zip(pesos, muestra)]
        resultado = get_resultado_actual(resultados)
        delta = taza * (resultado - salida)
        if(delta > 0):
            old_pesos = pesos
            pesos = actualiza_pesos(pesos, muestra, delta)
        else:
            if(old_pesos == pesos):
                return pesos
            else:
                print("Continua algoritmo...")

def get_resultado_actual(r):
    return next(r)

def actualiza_pesos(pesos, muestra, delta):
    n_pesos = []
    res = 0
    for m, p in zip(muestra, pesos):
        res = p + m*delta
        n_pesos.append(res)
    return n_pesos

def main():
    resultado = perceptron()

if __name__ == '__main__':
    main()
