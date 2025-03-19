##Dado um array de números inteiros de 1 a n (em que um número pode estar faltando), 
#encontre o número que está faltando.

array = [1, 2, 3, 5]
encontrado = 0

for i in range(len(array)):
    if array[i] - array[i - 1] > 1:
        encontrado =  array[i - 1] + 1
        print(f"Número ausente: {encontrado}")
        break
else:
    print("Não há números ausentes.")

