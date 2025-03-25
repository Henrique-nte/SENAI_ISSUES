#8 - Escreva um algoritmo que lê uma matriz M(5,5) e calcula as somas:

#a) da linha 4 de M.
#b) da coluna 2 de M.
#c) da diagonal principal.
#d) da diagonal secundária.
#e) de todos os elementos da matriz.
#f) Escreva estas somas e a matriz.

matriz = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1], #15
    [5, 6, 7, 8, 9], 
    [1, 1, 1, 1, 1], # 5
    [1, 2, 3, 4, 5]
]

#a) da linha 4 de M.
print("Soma da linha 4")
soma = 0
for i in range(5):
        if i == 3:
            for j in range(5):
                    soma += matriz[i][j] 
print(soma)

#b) da coluna 2 de M.
print("Soma da linha 2")
soma = 0
for i in range(5):
        if i == 1:
            for j in range(5):
                    soma += matriz[i][j] 
print(soma)

#c) da diagonal principal.
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            soma += matriz[i][j]
print(f"Soma da diagonal principal: {soma}")

#d) da diagonal secundária.    
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == len(matriz) - j:
                print(matriz[i][j])
                soma += matriz[i][j]

print(f"Soma da diagonal secundária: {soma}")

