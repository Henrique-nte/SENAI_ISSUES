#16 - Faça a rotação de um array para a direita k posições.

#Ex = array = 1, 2, 3, 4, 5  
#k = 2 saída= (4, 5, 1, 2, 3)

array = [1, 2, 3, 4, 5]

k = int(input("Quantas posições: "))

n = len(array)
k = k % n

for _ in range(k):
    temp = array[-1]
    for i in range(n - 1, 0, -1):
        array[i] = array[i - 1]
    array[0] = temp

print(array)



