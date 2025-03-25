#11 - Crie uma matriz 7X8 onde cada elemento é a soma dos índices de sua posição dentro da matriz;
matriz = []
i = 0
j = 0

for linha in range(7):
  linha = []
  for coluna in range(8):
    valor = i + j
    linha.append(valor)
    j += 1
  matriz.append(linha)
  i += 1
  j = 0

for linha in matriz:
  print(linha)