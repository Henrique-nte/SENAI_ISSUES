#Peça ao usuário uma lista de números e depois exiba essa lista ao contrário, 
#sem usar [::-1] ou reversed(), apenas laços de repetição.

array = [1, 2, 3, 4, 5]
lista = []
i = len(array)

while True:
    i -= 1
    lista.append(array[i])
    if i == 0:
        break

print(f"Array original: {array}")
print(f"Array ao contrario: {lista}")
    