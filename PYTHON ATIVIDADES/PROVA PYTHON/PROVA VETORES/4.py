#4.	Escreva um programa que leia um número N e crie um array de tamanho N 
#com números aleatórios entre 1 e 100. Em seguida, calcule e imprima a média
#dos números ímpares e a soma dos números pares.
import random
n = 5
array = []
soma = 0
media = 0
soma_pares = 0
contador = 0

for i in range(n):
    numeros_aleatorios = random.randint(1, 100)
    array.append(numeros_aleatorios)
    # média dos números ímpares
    if numeros_aleatorios % 2 != 0:  
        soma += numeros_aleatorios
        contador += 1
    #soma dos números pares.
    else:
        soma_pares += numeros_aleatorios

if contador > 0:
    media = soma / contador
print(f"Array: {array}")
print(f"Média dos números ímpares: {media:.2f}")
print(f"Soma dos números pares: {soma_pares}")

