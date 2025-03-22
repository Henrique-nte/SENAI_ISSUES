<<<<<<< Updated upstream
#19- Implemente um código que mova todos os números negativos para o início do array, mantendo
# a ordem dos outros números.

vetor = [1, 2, 3, 4, 5, -1, -2, -3]
negativos = []
lista = []
for i in range(len(vetor)):

    if vetor[i] < 0:

        negativos.append(vetor[i])
        vetor[i] = 0
        
i = 0
while i < len(vetor):
    if vetor[i] == 0:
        del vetor[i]
    else:
        i += 1

for i in range(len(negativos)):
    lista.append(negativos[i])
for i in range(len(vetor)):
    lista.append(vetor[i])
    
print(lista)
=======
#19- Implemente um código que mova todos os números negativos para o início 
# do array, mantendo a ordem dos outros números.
>>>>>>> Stashed changes
