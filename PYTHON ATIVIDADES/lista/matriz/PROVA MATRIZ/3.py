#Escreva um programa que leia os valores de faturas de 6 clientes durante 3 meses (matriz 6x3)
#e:
#○ Calcule o total faturado por cliente.
#○ Identifique o cliente com maior receita.
#○ Encontre o mês com maior faturamento total. 

matriz = [
    [1, 2, 5],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3] 
]

faturado = 0
maior_receita = float("-inf")
valor = float("-inf")

#○ Calcule o total faturado por cliente.
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        faturado += matriz[i][j]
    print(f"Para o Cliente {i + 1}, faturado: {faturado}")
    if faturado > maior_receita:
        maior_receita = faturado
    faturado = 0

#○ Identifique o cliente com maior receita.
print(f"Maior receita: {maior_receita}")
#○ Encontre o mês com maior faturamento total.
mes_faturamento_maior = 0  
soma_1 = 0
soma_2 = 0
soma_3 = 0
tamanho = len(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j == 0:
            soma_1 += matriz[i][j]
        if soma_1 > valor:
            mes_faturamento_maior = j + 1
            valor = soma_1
        elif j == 1:
            soma_2 += matriz[i][j]
        if soma_2 > valor:
            mes_faturamento_maior = j + 1
            valor = soma_2
        elif j == 2:
            soma_3 += matriz[i][j]
        if soma_3 > valor:
            mes_faturamento_maior = j + 1

print(f"Mês com maior faturamento: {mes_faturamento_maior}")


