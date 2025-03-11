#8- Dado um array com números positivos e negativos, crie um novo array 
#contendo apenas os números negativos, mas com seus sinais invertidos 
#(multiplicando-os por -1).

positivos = [1, 2, 3, 4]
negativos = [-1, -2, -3, -4]
print(f"Vetor postivo inicial: {positivos}")
print(f"Vetor negativo inicial: {negativos}")
novo = []
novo_2 = []


for i in range(len(positivos)):
    valor = positivos[i] * -1
    novo_2.append(valor)

print(f"Vetor positivo invertido: {novo_2}")

for i in range(len(negativos)):
    valor = negativos[i] * +1
    novo.append(valor)

print(f"Vetor negativo invertido: {novo}")






    