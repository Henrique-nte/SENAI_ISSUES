#4.	Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
media = 0

for i in range(5):
    numero = int(input(f"Digite o número {i + 1}:"))
    soma += numero
    media = soma / 5

print("VISÃO GERAL")
#soma dos números.
print(f"Soma dos números: {soma}")
#média dos números.
print(f"Média dos números: {media}")