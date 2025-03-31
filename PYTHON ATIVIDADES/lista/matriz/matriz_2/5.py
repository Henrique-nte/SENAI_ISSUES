#5 - Faça um algoritmo para ler uma matriz de 3×4 de números reais e depois exibir
# o elemento do canto superior e do canto inferior esquerdo.

matriz = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
]

for linha in matriz:  
    for elemento in linha: 
        print( elemento,"|", end=" ")
    print()
        
#elemento do canto superior esquerdo.
print(matriz[0][0])
#elemento do canto inferior esquerdo.
print(matriz[-1][0])