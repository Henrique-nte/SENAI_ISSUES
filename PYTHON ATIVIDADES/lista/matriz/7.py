#7 - Escrever um algoritmo para ler uma matriz (7,4) contendo valores inteiros 
#(supor que os valores são distintos). Após, encontrar o menor valor contido
#na matriz e sua posição.

matriz = 0
valor_menor = float("inf")


for linha in range(2):
    for coluna in range(2):
        valor = int(input("Digite um valor:"))
        linha.append(valor)
    matriz.append(linha)

