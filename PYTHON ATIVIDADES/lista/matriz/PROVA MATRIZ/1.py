#Crie um programa que leia uma matriz 3x3 de inteiros e calcule o produto de todos os elementos
#da segunda linha.

matriz = [
    [1, 2, 3],
    [5, 5, 5],
    [3, 2, 1]
]

soma = 0

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == 1:
            soma += matriz[i][j]

print(soma)