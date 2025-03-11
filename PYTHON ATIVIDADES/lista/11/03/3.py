#3- Faça um algoritmo que, para um vetor X de 15 elementos inteiros, transforme para zero todos os elementos que 
#receberem valores negativos, em seguida, exiba o vetor com as alterações.

vetor = []

for i in range(5):
    valor = int(input("Digite um número inteiro: "))
    vetor.append(valor)

    if valor < 0:
        vetor[i] = 0

print(vetor)