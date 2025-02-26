#Escreva um programa que encontre o maior e menor número em
#uma lista de 10 números randômicos
import random
i = 0
maior = 0
menor = float("inf")
while i < 10:
    i += 1
    numeros_aleatorio = random.randint(1, 100)
    print(f"Número - {i}: {numeros_aleatorio}")
    if numeros_aleatorio > maior:
        maior = numeros_aleatorio
    elif numeros_aleatorio < menor:
        menor = numeros_aleatorio

print(f"MAIOR: {maior}")
print(f"MENOR: {menor}")