#2.	Faça um programa que leia um array de 7 números e, em seguida, 
#imprima todos os números que são maiores que 10.

array = []
maiores_que_10 = []
verificador = 0

for i in range(7):
    numero = float(input("Digite um número: "))
    array.append(numero)

for i in range(len(array)):
    if array[i] > 10:
        maiores_que_10.append(array[i])
    elif array[i] <= 10:
        verificador += 1

if verificador == len(array):
    print("Não há números maiores que 10.")
else:
    print(f"Números maiores que 10: {maiores_que_10}")