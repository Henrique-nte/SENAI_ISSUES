#18- Implemente um código que conte quantas vezes um determinado número aparece em um array.

vetor = [1, 2, 3, 4, 5, 1, 1, 1]
print(vetor)
contador = 0

numero = int(input("Digite um determinado número: "))

for i in range(len(vetor)):
    if numero == vetor[i]:
        contador += 1

print(contador)
