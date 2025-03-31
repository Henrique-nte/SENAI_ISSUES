#9 - Ler uma matriz 5X5 e gerar outra em que cada elemento é o cubo do elemento
#  respectivo na matriz original.

matriz = [
    [3,2,],
    [3,2,]  
]

lista = []
for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz)):
        valor = matriz[i][j] ** 3
        linha.append(valor)
    lista.append(linha)

for l,c in matriz:
    print(l,"|", c)     
print()
for l,c in lista:
    print(l,"|", c)
 