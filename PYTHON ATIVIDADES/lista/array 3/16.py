#16 - Faça a rotação de um array para a direita k posições.

#Ex = array = 1, 2, 3, 4, 5  
#k = 2 saída= (4, 5, 1, 2, 3)

array = [1, 2, 3, 4, 5]
print(f"1 - {array}")

k = int(input("Quantas posições: "))
n = len(array)
k = k % n

for i in range(k):

    

    print(f"2 - {array}")

print(f"3 - {array}")