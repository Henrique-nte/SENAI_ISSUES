#3.	Faça um programa que leia um número n e mostre na tela os n  
#e depois os n primeiros números ímpares

n = int(input("N = "))
j = 0

#primeiros números pares
print("Números pares: ")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"{i}")

#primeiros números ímpares
print("Números Impares: ")
for j in range(1, n + 1):
        if j % 2 != 0:
            print(f"{j}")