#8 - Escreva um algoritmo que lê uma matriz M(5,5) e calcula as somas:

#a) da linha 4 de M.
#b) da coluna 2 de M.
#c) da diagonal principal.
#d) da diagonal secundária.
#e) de todos os elementos da matriz.
#f) Escreva estas somas e a matriz.

matriz = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
]

#a) da linha 4 de M.
for i in range(5):
    for j in range(5):
        if i 