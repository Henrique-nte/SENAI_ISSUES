#4 - Ler uma matriz 5X5 e gerar outra em que cada elemento é o cubo do elemento
# respectivo na matriz original.

matriz = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [3, 9, 8, 2, 0],
    [1, 3, 5, 7, 8],
    [1, 2, 3, 4, 5],
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