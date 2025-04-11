#Desenvolva um programa que leia uma matriz 5x5 e exiba apenas os elementos que formam a
#cruz central (linha 3 e coluna 3)

matriz = [
    [1, 2, 0, 4, 5],
    [1, 2, 0, 4, 5],
    [1, 1, 0, 1, 1],
    [1, 2, 0, 4, 5],
    [1, 2, 0, 4, 5]
]

print("Elementos da linha 3")
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == 2:
            print(matriz[i][j])

print("Elementos da coluna 3")
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if j == 2:
            print(matriz[i][j])