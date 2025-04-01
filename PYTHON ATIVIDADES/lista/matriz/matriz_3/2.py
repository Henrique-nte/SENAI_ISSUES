#2 - Criar uma matriz que pede um valor, e exiba conforme a seguinte tabela.
import random

n = int(input("Digite um valor: "))
matriz= []

for linha in range(n):
    linha = []
    for coluna in range(n):
        valor = random.randint(10, 30)
        if valor not in linha:
            linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for elemento in linha:
        print(elemento,"|", end = "")
    print()

for i in range(len(matriz)):
    
    for j in range(1, len(matriz[i])):
        print(matriz[i][j])
    
        