#3.	Crie um programa que leia 15 números inteiros e construa um novo array
# onde cada elemento seja o dobro do número correspondente no array original.

array = []
lista = []

for i in range(5):
    numero = int(input("Digite um número: "))   
    array.append(numero)

for i in range(len(array)):
    valor = array[i] * 2
    lista.append(valor)

print(f"Array original: {array}")
print(f"Array novo: {lista}")