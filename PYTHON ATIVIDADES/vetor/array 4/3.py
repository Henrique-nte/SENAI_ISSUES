#Crie um programa que leia 15 números inteiros e construa um novo array
# onde cada elemento seja o dobro do número correspondente no array original.

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
new_array = []

for i in range(len(array)):
    valor = array[i] * 2
    new_array.append(valor)

print(new_array)
print(array)