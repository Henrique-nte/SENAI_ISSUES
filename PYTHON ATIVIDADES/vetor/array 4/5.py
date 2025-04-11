#Crie um programa que receba um valor inteiro e:

#   Exiba "Número válido" caso ele esteja entre 20 e 90 (inclusive).
#   Exiba "Número inválido" caso contrário.

n = int(input("Digite um número inteiro: "))

if n > 20 and n < 90:
    print("Número válido")
else:
    print("Número inválido")