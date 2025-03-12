numeros = []

for i in range(5):
    valor = int(input("Digite um valor: "))
    numeros.append(valor)

media = sum(numeros) / len(numeros)
print(media)