#14 - Você recebe um vetor de números inteiros. Escreva um programa em JS que determine a moda do vetor, ou seja,
#  o elemento que mais frequentemente aparece. Se houver mais de um elemento com a mesma frequência máxima, 
# retorne todos eles.

# Recebendo o vetor

vetor = []

repetidos = []

for i in range(7):

    valor = int(input("Digite um número inteiro: "))
    vetor.append(valor)

for i in range(len(vetor)):
        
        for j in range(i + 1, len(vetor)):

            if vetor[i] == vetor[j] and vetor[i] not in repetidos:

                repetidos.append(vetor[i])
                
#for num in repetidos:
    #if num not in repetidos_unicos:
        #repetidos_unicos.append(num)

print(repetidos)
           
#max_frequencia = -1

#for i in range(len(repetidos)):
    #if frequencia_total[i] > max_frequencia:
        #max_frequencia = frequencia_total[i]
        #moda = repetidos[i]


