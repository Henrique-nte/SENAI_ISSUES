#14 - Você recebe um vetor de números inteiros. Escreva um programa em JS que determine a moda do vetor, ou seja,
#  o elemento que mais frequentemente aparece. Se houver mais de um elemento com a mesma frequência máxima, 
# retorne todos eles.

vetor = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7]
lista = []
contador = 0
#Guardar em dois vetores e analisar se sao iguais
for i in range(len(vetor)):

    if vetor[i] == vetor[i - 1]:
        contador += 1
        lista.append(vetor[i])
    
    

print(lista)