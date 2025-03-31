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
soma_4 = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == 3:
            soma_4 += matriz[i][j]

            
#b) da coluna 2 de M.
soma_2 = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if j == 1:
            soma_2 += matriz[i][j]


#c) da diagonal principal.
soma_principal = 0
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            soma_principal += matriz[i][j]

#d) da diagonal secundária.
soma_secundaria = 0
n = len(matriz)
i = 0
while i < len(matriz):
    j = n - i - 1 
    soma_secundaria += matriz[i][j]
    i += 1
#e) de todos os elementos da matriz.
soma_todos = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        soma_todos += matriz[i][j]
#f) Escreva estas somas e a matriz.

print(f"Soma da linha 4 de M: {soma_4}")
print(f"Soma da coluna 2 de M: {soma_2}")
print(f"Soma da diagonal principal: {soma_principal}")
print(f"Soma da diagonal secundária: {soma_secundaria}")
print(f"Soma de todos elementos da matriz: {soma_todos}")