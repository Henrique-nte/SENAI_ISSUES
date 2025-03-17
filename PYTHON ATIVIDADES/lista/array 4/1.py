#Escreva um programa que leia 10 números e calcule a soma
# de todos os números ímpares.

vetor = []
soma = 0
contador = 0
impares = []

for i in range(5):
    valor = int(input(f"Digite o número {i + 1}:"))
    vetor.append(valor)
    if valor % 2 != 0:
        impares.append(valor)
        soma += valor
        contador += 1

media = soma / contador
print(f"Números impares: {impares}")
print(f"Media dos números impares: {media}")