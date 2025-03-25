#2- Criar uma matriz de 5x5 que mostre quando os índices forem iguais

matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

<<<<<<< HEAD
for i in range(len(matriz)):
    for j in range(i + 1,len(matriz)):
        if matriz[i][j] == matriz[i][j]:
            
            indice_i = i
            indice_j = j
print(f"Indices {matriz[indice_i][indice_j]} iguais")
=======
for i in range (len(matriz)):
  for j in range (len(matriz)):
    if i == j:
      print(matriz[i][j])

>>>>>>> 6f1ceacdc886621d4cec7a5200f3f735827b930a
