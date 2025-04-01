#1 - Criar um programa que leia os elementos de uma matriz inteira 4 x 4 e:
#a) escreva os elementos da diagonal principal;
#b) escreva todos os elementos, exceto os elementos da diagonal principal;

matriz = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
]
#a) escreva os elementos da diagonal principal;
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            print(matriz[i][j])
#b) escreva todos os elementos, exceto os elementos da diagonal principal;
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i != j:
            print(matriz[i][j], end = "")
        print()