#2- Faça um programa em JS que leia um vetor de seis elementos numéricos inteiros, calcule e mostre:
 
#a) A quantidade de números pares 
#b) Quais os números pares 
#c) A quantidade de números ímpares 
#d) Quais os números ímpares

numeros = []
pares = []
impares = []

for i in range(6):
    valor = int(input(f"Digite o numero {i + 1}:"))
    numeros.append(valor)

    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 != 0:
        impares.append(valor)

print(f"Quantidade números pares: {pares}")
print(f"Quantidade números pares: {impares}")