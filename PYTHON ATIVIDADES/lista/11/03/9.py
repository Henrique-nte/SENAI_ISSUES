#9 -Faça um programa que leia 10 números inteiros, armazene-os em um vetor, solicite um valor de
#referência inteiro e:
#a) imprima os números do vetor que são maiores que o valor referência
#b) retorne quantos números armazenados no vetor são menores que o valor de referência
#c) retorne quantas vezes o valor de referência aparece no vetor

vetor = []

for i in range(3):
    valor = int(input(F"Digite o número {i + 1}: "))
    vetor.append(valor)

value = int(input("Valor de referência: "))

#a) imprima os números do vetor que são maiores que o valor referência
for i in range(3):
    if vetor[i] > value:
        print(f"Números do vetor que são maiores que o valor de referência: {vetor[i]}")

#b) retorne quantos números armazenados no vetor são menores que o valor de referência
contador = 0
for i in range(3):
    
    if vetor[i] < value:
        contador += 1
print(f"Quantidade de números armazenados no vetor que são menores que o valor de referência: {contador}")

#c) retorne quantas vezes o valor de referência aparece no vetor
verificador = 0
for i in range(3):
    if vetor[i] == value:
        verificador += 1
print(f"Quantas vezes o valor de referência aparece no vetor: {verificador}")
    