#2- Criar uma matriz de 5x5 que mostre quando os índices forem iguais

matriz = [
    [1,2,3,5],
    [2,3,4,5]
]

for i in range(len(matriz)):
    for j in range(i + 1,len(matriz)):
        if matriz[i][j] == matriz[i][j]:
            
            indice_i = i
            indice_j = j
print(f"Indices {matriz[indice_i][indice_j]} iguais")