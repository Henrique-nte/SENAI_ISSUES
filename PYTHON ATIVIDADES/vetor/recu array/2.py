#2-Faça um programa que armazene as horas trabalhadas de 5 funcionários em uma semana. 
#Depois, calcule o total de horas trabalhadas e mostre o valor a ser pago a cada um, 
#sabendo que a hora de trabalho custa R$ 20.

matriz = [
    [5, 6, 7, 8, 9],
    [5, 4, 7, 8, 5],
    [5, 6, 7, 2, 9],
    [9, 6, 7, 8, 9],
    [1, 2, 3, 4, 5]
]

soma = 0

for i in range(len(matriz)):
    for j in range(len(matriz)):
        soma += matriz[i][j]
    resul = 20 * soma
    print(f"Soma das horas trabalhadas na semana do fun {i + 1}: {soma}")
    print(f"Valor a ser pago para o fun {i + 1}: {resul}")
    soma = 0
    resul = 0