#Dado um array de números, crie um novo array onde o valor em cada posição é o número de 
#elementos menores do que o número correspondente da posição no array original. A solução não 
#pode usar a comparação direta entre todos os elementos.
#array = [5, 2, 6, 1, 7]
# Resultado esperado: [2, 1, 3, 0, 4]
# Explicação: Para cada elemento, contamos quantos elementos 
#são menores do que ele.


import inspect


array = [5, 2, 6, 1, 7]
lista = []
contador = 0

for i in range(len(array)):
    contador = 0
    
    for j in range (len(array)):
        if array[i] > array[j]:
            contador += 1
    lista.append(contador)


print(lista)