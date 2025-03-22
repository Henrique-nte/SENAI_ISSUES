#16 - Faça a rotação de um array para a direita k posições.

#Ex = array = [1, 2, 3, 4, 5]
#k = 2 saída= [4, 5, 1, 2, 3]

array = [1, 2, 3, 4, 5]

k = int(input("Quantas posições: "))

n = len(array)
k = k % n

<<<<<<< Updated upstream
for _ in range(k):
    temp = array[-1]
    for i in range(n - 1, 0, -1):
        array[i] = array[i - 1]
    array[0] = temp

print(array)



=======
# Rotaciona o array movendo os elementos um por um
for _ in range(k):
    ultimo = array[-1]  # Pega o último elemento
    for i in range(n - 1, 0, -1):
        array[i] = array[i - 1]  # Move os elementos para a direita
    array[0] = ultimo  # Coloca o último elemento no início

print(array)   
>>>>>>> Stashed changes
