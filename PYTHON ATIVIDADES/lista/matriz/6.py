#6 – Escreva um algoritmo para armazenar valores inteiros em uma matriz (5,5). A seguir,
#calcular a média dos valores pares contidos na matriz e escrever seu conteúdo.

matriz = []

for linha in range(2):
    linha = []
    for coluna in range(2):
        valor = int(input("Digite um número: "))
        linha.append(valor)
    matriz.append(linha)

soma_pares = 0

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]

print(soma_pares)