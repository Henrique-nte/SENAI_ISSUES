#matriz 6X3
matriz = [
    [1, 2, 3],
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
soma = 0

i = 0
j = 0
contador = 0

for j in range(len(matriz[0])):  
    soma = 0
    for i in range(len(matriz)):  
        soma += matriz[i][j]
    print(soma)
    if soma > valor:
        valor = soma
        mes_faturamento_maior = j



print(f"Mês com maior faturamento: {mes_faturamento_maior}")