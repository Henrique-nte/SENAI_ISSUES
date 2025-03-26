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
    [1, 1, 1, 1, 1], # 5
    [1, 2, 3, 4, 5] #15
]

#a) da linha 4 de M.

soma = 0
for i in range(5):
        if i == 4:
            for j in range(5):
                    soma += matriz[i][j] 
print(f"Soma da linha 4: {soma}")

#b) da coluna 2 de M.

soma = 0
for i in range(5):
        for j in range(5):
            if j == 2:
                soma += matriz[i][j] 
print(f"Soma da coluna 2: {soma}")

#c) da diagonal principal.
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            soma += matriz[i][j]
print(f"Soma da diagonal principal: {soma}")

#matriz = [
    #[1, 2, 3, 4, 5],
    #[5, 4, 3, 2, 1], #15
    #[5, 6, 7, 8, 9], 
    #[1, 1, 1, 1, 1], # 5
    #[1, 2, 3, 4, 5]
#]
#d) da diagonal secundária.  #16  
soma = 0
#Lógica é j = n - 1 - i
n = len(matriz)  
for i in range(n):
    j = n - 1 - i  
    if  j < n >= 0:  
        soma += matriz[i][j]

print(f"Soma da diagonal secundária: {soma}")

#e) de todos os elementos da matriz.
print("Elementos da matriz")
for linha in matriz:  
    for elemento in linha: 
        print(elemento,"|", end=" ")  
    print()  