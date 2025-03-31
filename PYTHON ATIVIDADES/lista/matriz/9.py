#9 - Ler uma matriz 5X5 e gerar outra em que cada elemento é o cubo do elemento
#  respectivo na matriz original.

matriz = [
    [8, 3, 5, 1, 7],
    [4, 9, 2, 6, 3],
    [7, 1, 8, 4, 5],
    [2, 6, 3, 9, 8],
    [5, 7, 4, 2, 1]
]

lista = []
for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz)):
        valor = matriz[i][j] ** 3
        linha.append(valor)
    lista.append(linha)

for linha in matriz:
    for elemento in linha:
        print( elemento,"|", end=" ")
    print()

print()

for linha in lista:
    for elemento in linha:
        print( elemento,"|", end=" ")
    print()
 