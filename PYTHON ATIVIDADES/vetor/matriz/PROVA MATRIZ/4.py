#Crie um algoritmo que gere uma matriz com dimensões definidas pelo usuário (linha x coluna),
#preencha com números inteiros aleatórios, e calcule a soma de todos os elementos positivos.

import random

x = int(input("Quantas linhas deseja na matriz?"))
y = int(input("Quantas colunas deseja na matriz?"))
matriz = []

for linha in range(x):
    linha = []
    for coluna in range(y):
        numero_aleatorio = random.randint(1, 100)
        valor = numero_aleatorio
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for elemento in linha:
        print(elemento)