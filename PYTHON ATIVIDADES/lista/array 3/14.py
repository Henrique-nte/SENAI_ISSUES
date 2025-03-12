#14 - Você recebe um vetor de números inteiros. Escreva um programa em JS que determine a moda do vetor, ou seja,
#  o elemento que mais frequentemente aparece. Se houver mais de um elemento com a mesma frequência máxima, 
# retorne todos eles.

vetor = [1, 2, 2, 3, 4, 5, 6, 6, 6]
lista = []
for i in range(len(vetor)):
    
    if vetor[i] == vetor[i - 1]:
        lista.append(vetor[i])

print(lista)