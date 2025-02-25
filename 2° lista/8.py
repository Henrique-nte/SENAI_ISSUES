# 8 - Peça ao usuário um número inteiro positivo e exiba todos os números pares
#de forma decrescente até chegar a zero. O programa deve exibir a sequência
#de forma organizada, considerando que o número de entrada pode ser par ou ímpar.
numero = int(input("Digite um número: "))

if numero % 2 == 1:
    numero -= 1

while numero >= 0:
    print(numero)
    numero -= 2