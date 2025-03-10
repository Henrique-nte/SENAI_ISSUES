#Faça um programa que leia e mostre dois vetores numericos inteiros com 20 numeros cada. 
#depois de montados gere um terceiro vetor formado pela diferenca dos dois vetores lidos, 
#um quarto vetor formado pela soma dos dois vetores lidos e por ultmo um quinto vetor formado 
#pela multiplicacao dos dois vetores lidos

vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 20
vetor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 20
vetor3 = []
vetor4 = []
vetor5 = []

for i in range(10):
    valor = vetor1[i] - vetor2[i]
    vetor3.append(valor)

    valor = vetor1[i] + vetor2[i]
    vetor4.append(valor)

    valor = vetor1[i] * vetor2[i]
    vetor5.append(valor)

print(f"Vetor 1: {vetor1}")
print()
print(f"Vetor 2: {vetor2}")
print()
print(f"Diferença: {vetor3}")
print()
print(f"Soma: {vetor4}")
print()
print(f"Multiplicação: {vetor5}")
print()