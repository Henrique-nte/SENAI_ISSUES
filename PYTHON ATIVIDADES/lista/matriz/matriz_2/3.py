#3 - Escreva um algoritmo que lê uma matriz M(5,5) e calcula as somas:
#a) da linha 4 de M.
#b) da coluna 2 de M.
#c) da diagonal principal.
#d) da diagonal secundária.
#e) de todos os elementos da matriz.
#f) Escreva estas somas e a matriz.

matriz = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [9, 8, 7, 6, 5],
    [4, 3, 2, 1, 5],
    [3, 4, 9, 4, 5]
]
#a) da linha 4 de M.
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == 4:
            soma += matriz[i][j]

            
#b) da coluna 2 de M.
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if j == 1:
            soma += matriz[i][j]


#c) da diagonal principal.
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            soma += matriz[i][j]

#d) da diagonal secundária.
n = len(matriz)

while 