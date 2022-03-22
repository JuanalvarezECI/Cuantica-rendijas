'''GRUPO JUAN JOSE ALVAREZ  ; JHONATHAN GOMEZ ; BRAYAN TINJACA'''
import main as vm
import matplotlib.pyplot as plot
import numpy as np

def action(m1, v1):
    if len(m1[0]) == len(v1):
        m = [[0 for i in range(len(v1[0]))] for j in range(len(m1))]
        for fila in range(len(m1)):
            for columna in range(len(v1[0])):
                for aux in range(len(m1[0])):
                    m[fila][columna] = round(m[fila][columna] + (m1[fila][aux] * v1[aux][columna]), 3)
        return m
def probabiliscocuantico(matriz, v, c):
    if (c >= 0) and (type(c) is int):
        length = len(v)
        matrizb = matriz[:]
        for x in range(c):
            matriz = main.productoMatrices(matriz, matrizb)

        return matrizfinal(matriz)
    return -1


def matrizfinal(matriz):
    fila, columna = len(matriz), len(matriz[0])
    for i in range(fila):
        nfila = []
        for j in range(columna):
            nfila.append([(main.Modulo(matriz[i][j]) ** 2), 0])

        matriz[i] = nfila
    return matriz
def rendijasprobabilistico(matrix, vector, t):
    ans = vector
    for i in range(t):
        ans = action(matrix, ans)
    return ans
def rendijascuantico(matriz, v, c):
    return probabilisticocuantico(matriz, v, c)
def vectordeestados(probs):
    estados = [x for x in range(len(probs))]
    fig, ax = plt.subplots()
    ax.set_ylabel('Probabilidades')
    ax.set_xlabel('Estados')
    ax.set_title('Sistema Cuantico')
    plt.bar(estados, probs)
    plt.savefig('probabilities.png')
    plt.show()
