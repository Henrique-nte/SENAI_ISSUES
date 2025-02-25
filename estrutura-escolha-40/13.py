#13.	Verificar se um número é par ou ímpar
#Peça para o usuário inserir um número e mostre se ele é "Par" ou "Ímpar".

numero = float(input("Digite um número: "))

if numero % 2 == 0:
    print("Par")
elif numero % 2 == 1:
    print("Ímpar")
