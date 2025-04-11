#Faça um programa que leia um array de 7 números e, em seguida, 
#imprima todos os números que são maiores que 10.

array = [1, 20, 3, 4, 5, 6, 11]

for i in range(len(array)):
    if array[i] > 10:
        print(array[i])