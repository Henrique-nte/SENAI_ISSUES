#17- Implemente um código que mova todos os elementos 0 de um array para o final, mantendo 
#a ordem dos outros elementos.

array = [1, 2, 0, 0, 3, 0 , 0]
zeros = []
i = 0
contador = 0

while i < len(array):
    if array[i] == 0:
        contador += 1
        del array[i]
    else:
        i += 1
        
for i in range(contador):
    array.append(0)

        
print(array)