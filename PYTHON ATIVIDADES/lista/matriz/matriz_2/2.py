#2 - Escrever um algoritmo para ler uma matriz (7,4) contendo valores inteiros 
#(supor que os valores são
#distintos). Após, encontrar o menor valor contido na matriz e sua posição.

matriz = [
    [3, 12, 25, 7],
    [8, 19, 34, 2],
    [15, 28, 9, 41],
    [22, 5, 37, 16],
    [30, 1, 48, 11],
    [6, 23, 40, 29],
    [14, 33, 4, 18]
]

valor_menor = float("inf")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] < valor_menor:
            valor_menor = matriz[i][j]
            posicao_i = i
            posicao_j = j 

print(f"Menor valor: {valor_menor}")
print(f"Posição: Linha: [{posicao_i}] Coluna: [{posicao_j}]")