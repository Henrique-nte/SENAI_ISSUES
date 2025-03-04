#Escreva um programa que peça dois números inteiros positivos ao usuário e use um laço 
#de repetição para somar todos os números ímpares entre esses dois valores.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um segundo número: "))
soma = 0
i = 0

for i in range(n1, n2 + 1):
    if i % 2 != 0:
        print(f"Impar: {i}")
        soma += i

print(f"Soma: {soma}")

    