#20- Implemente um código que mescle dois arrays, mas sem adicionar elementos duplicados. 
#O resultado deve ser uma lista contendo todos os elementos dos dois arrays sem repetições.

vetor = [1, 1, 2, 3, 4, 5]
vetor_2 = [1, 1, 2, 3, 4, 5]

lista = []

for i in range(len(vetor)):

    if vetor[i] not in lista:
        lista.append(vetor[i])
        
    if vetor_2[i] not in lista:
        lista.append(vetor_2[i])

print(lista)