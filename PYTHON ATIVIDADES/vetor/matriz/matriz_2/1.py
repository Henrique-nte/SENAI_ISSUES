#1 – Escreva um algoritmo para armazenar valores inteiros em uma matriz (5,5).
# A seguir, calcular a média dos valores pares contidos na matriz e escrever seu conteúdo.

matriz = [
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1]
    
]

pares = 0
soma_pares = 0

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] % 2 == 0:
            pares += 1
            soma_pares += matriz[i][j]

media = soma_pares / pares

print(f"Média: {media:.2f}")