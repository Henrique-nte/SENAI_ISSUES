#7 - Escrever um algoritmo para ler uma matriz (7,4) contendo valores inteiros 
#(supor que os valores são distintos). Após, encontrar o menor valor contido
#na matriz e sua posição.

matriz = [
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [6, 7, 8, 9],
    [14, 13, 12, 11]
]
valor_menor = float("inf")

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] < valor_menor:
            valor_menor = matriz[i][j]

print(valor_menor)