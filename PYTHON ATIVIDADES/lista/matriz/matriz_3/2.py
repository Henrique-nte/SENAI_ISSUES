#2 - Criar uma matriz que pede um valor, e exiba conforme a seguinte tabela.
import random

n = int(input("Digite um valor: "))
matriz= []

for linha in range(n):
    linha = []
    for coluna in range(n):
        valor = random.randint(1, 9)
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for elemento in linha:
        print(elemento,"|", end = "")
    print()

print("Diagonal principal")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j == i:
            print(matriz[i][j], "|", end = "")
print()
print("Diagonal secundária")
n = len(matriz)
for i in range(n):
    j = n - 1 - i  
    if  j < n >= 0:  
            print(matriz[i][j], "|", end = "")
    
        