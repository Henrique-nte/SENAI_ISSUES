#6- Crie um programa que gere um vetor com 100 números inteiros aleatórios entre 1 e 1000.
# Calcule a média desses números.

import random

soma_aleatorios = 0
numeros_aleatorios = [random.randint(1, 1000) for _ in range(10)]

print(numeros_aleatorios)
for i in range(len(numeros_aleatorios)):
  soma_aleatorios += numeros_aleatorios[i]

media = soma_aleatorios / len(numeros_aleatorios)
print(media)