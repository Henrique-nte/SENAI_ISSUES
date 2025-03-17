#Escreva um programa que leia um número N e crie um array de tamanho N 
#com números aleatórios entre 1 e 100. Em seguida, calcule e imprima a média 
#dos números ímpares e a soma dos números pares.
import random
array = []
soma_aleatorios = 0
soma_pares = 0
soma_impares = 0
media_impares = 0
contador = 0

n = int(input("Quantos números você deseja: "))

numeros_aleatorios = [random.randint(1, 100) for _ in range(n)]
array.append(numeros_aleatorios)

print(numeros_aleatorios)

for i in range(len(numeros_aleatorios)):

    if numeros_aleatorios[i] % 2 != 0:
        soma_impares += numeros_aleatorios[i]
        contador += 1
    else:
        soma_pares += numeros_aleatorios[i]
        
if contador > 0:
    media_impares = soma_impares / contador

print(f"Média dos numeros impares: {media_impares:.2f}")
print(f"Soma dos numeros pares: {soma_pares}")
