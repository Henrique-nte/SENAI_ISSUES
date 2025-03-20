#1.	Escreva um programa que leia 10 números e calcule 
#a soma de todos os números ímpares. 
soma = 0
lista = []

for i in range(10):
    numero = int(input("Digite um número: "))

    #a soma de todos os números ímpares
    if numero % 2 != 0:
        lista.append(numero)
        soma += numero

print(lista)
print(f"Soma dos números impares: {soma}")