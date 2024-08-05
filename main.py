def analizar_matriz(matriz):
    from collections import Counter

    # Convertir la matriz en una lista unidimensional
    numeros = [num for fila in matriz for num in fila]

    # Contar la frecuencia de cada número
    frecuencia = Counter(numeros)

    # Contar los números que aparecen solo una vez y los que se repiten
    solo_una_vez = sum(1 for count in frecuencia.values() if count == 1)
    repetidos = sum(1 for count in frecuencia.values() if count > 1)

    return [solo_una_vez, repetidos]


def pares_que_suman_n(n):
    pares = []
    for i in range(1, n//2 + 1):
        pares.append((i, n - i))
    return pares


print(analizar_matriz([[2, 2], [2, 2]]))
print(analizar_matriz([[2, 1, 3], [4, 5, 2], [6, 6, 6]]))

print(pares_que_suman_n(5))
print(pares_que_suman_n(10))
