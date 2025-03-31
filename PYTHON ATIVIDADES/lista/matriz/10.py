#10 - Faça um algoritmo para ler uma matriz de 3×4 de números reais e depois exibir 
# o elemento do canto superior e do canto inferior esquerdo.

matriz = []

for i in range(3):
    linha = []
    for j in range(4):
        valor = float(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)


for linha in matriz:  
    for elemento in linha: 
        print( elemento,"|", end=" ")
    print()
        
#elemento do canto superior esquerdo.
print(matriz[0][0])
#elemento do canto inferior esquerdo.
print(matriz[-1][0])