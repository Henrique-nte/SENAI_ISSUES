#6 - Crie uma matriz 7X8 onde cada elemento é a soma dos índices de sua posição dentro da matriz;

matriz = []
for i in range(7):
    linha = []
    for j in range(8):
        valor = i + j
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:  
    for elemento in linha: 
        print( elemento,"|", end=" ")
    print()