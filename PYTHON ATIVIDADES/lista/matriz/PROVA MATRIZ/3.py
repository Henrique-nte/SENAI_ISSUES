#Escreva um programa que leia os valores de faturas de 6 clientes durante 3 meses (matriz 6x3)
#e:
#○ Calcule o total faturado por cliente.
#○ Identifique o cliente com maior receita.
#○ Encontre o mês com maior faturamento total. 

matriz = [
    [1, 2, 3],
    [3, 1, 2],
    [5, 2, 1],
    [9, 4, 7],
    [6, 2, 3],
    [1, 2, 6] 
]

faturado = 0
maior_receita = float("-inf")

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

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        faturado += matriz[i][j]
        print(faturado)
        if faturado > mes_faturamento_maior:
            mes_faturamento_maior = j
        faturado = 0

print(f"Mês com maior faturamento: {mes_faturamento_maior}")


