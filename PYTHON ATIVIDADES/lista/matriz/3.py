#3- Escreva um programa que leia uma matriz 4 x 4 de inteiros e atribua o valor 0 para
# os valores negativos, e mostre todos os valores da matriz.
matriz = []

for linha in range(4):
    linha = []
    for coluna in range(4):
      valor = int(input("Digite um número: "))
      if valor < 0:
        valor = 0
      linha.append(valor)
    matriz.append(linha)

for linha in matriz:  
    for elemento in linha: 
        print( elemento,"|", end=" ")
    print()
