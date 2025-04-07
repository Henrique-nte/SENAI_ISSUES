#5- Criar um programa que leia os elementos de uma matriz inteira 4 x 4 e:
#a) escreva os elementos da diagonal principal;
#b) escreva todos os elementos, exceto os elementos da diagonal principal;

matriz = []

for linha in range(3):
    linha = []
    for coluna in range(3):
        valor = int(input("Digite um número:"))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz: 
    print(f"{linha}")

#a) escreva os elementos da diagonal principal;
print("Elementos da diagonal da matriz")
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            
            print(matriz[i][j], "|", end=" ")
        
print()
print("Elementos exceto os da diagonal")
#b) escreva todos os elementos, exceto os elementos da diagonal principal;
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i != j:
            print(matriz[i][j], "|", end=" ")