#4-Escreva um programa que leia uma matriz 6 x 6 de inteiros. Leia também um valor
#inteiro x. O programa deverá fazer uma busca desse valor na matriz e, ao final
#escrever sua localização (linha e coluna) ou uma mensagem de “não encontrado”.

matriz = [
  [1, 2, 3, 4, 5, 6],
  [7, 8, 9, 10, 11, 12],
  [13, 14, 15, 16, 17, 1],
  [19, 20, 21, 22, 23, 24],
  [25, 26, 27, 28, 29, 30],
  [31, 32, 33, 34, 35, 36]
]

x = int(input("Digite um valor para ser encontrado: "))
encontrado = 0

for linha in range(len(matriz)):
  for coluna in range(len(matriz)):
    if matriz[linha][coluna] == x:
      encontrado = 1
      print(f"Localização: linha: {linha} coluna: {coluna}")

if encontrado == 0:
  print("Não encontrado.")
