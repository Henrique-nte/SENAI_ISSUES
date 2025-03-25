#3- Escreva um programa que leia uma matriz 4 x 4 de inteiros e atribua o valor 0 para
# os valores negativos, e mostre todos os valores da matriz.
matriz = []

for linha in range(2):
    linha = []
    for coluna in range(2):
      valor = int(input("Digite um número: "))
      if valor < 0:
        valor = 0
      linha.append(valor)
    matriz.append(linha)

for l,c in matriz: 
    print(str(l) + " | " + str(c))
