#3.	Faça um programa que leia um número n e mostre na tela os n  
#e depois os n primeiros números ímpares

n = int(input("N = "))

#primeiros números pares
print("Números pares: ")
for pares in range(1, n + 1):
    if pares % 2 == 0:
        print(f"{pares}")

#primeiros números ímpares
print("Números Impares: ")
for impares in range(1, n + 1):
        if impares % 2 != 0:
            print(f"{impares}")