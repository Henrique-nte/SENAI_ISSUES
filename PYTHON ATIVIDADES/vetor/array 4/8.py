#Você recebe um array de vendas diárias de uma loja e precisa calcular a soma total
#das vendas, o valor médio das vendas e a maior venda registrada. Além disso, o 
#algoritmo deve identificar se houve algum dia com vendas abaixo de um valor mínimo esperado.


soma_total = 0
maior_venda = float("-inf")
dia = 0
valor_mínimo = int(input("Qual o valor mínimo esperado: "))
array = []
for i in range(5):

    valor = int(input(f"Valor da venda no dia {i + 1}:"))
    array.append(valor)

    soma_total += valor
    
    if valor > maior_venda:
        maior_venda = valor

valor_medio = soma_total / len(array)

print(f"Soma total das vendas: {soma_total}")
print(f"Maior venda registrada: {maior_venda}")
print(f"Valor médio: {valor_medio}")
dias = []
valor_abaixo = []

for i in range(len(array)):
    if array[i] < valor_mínimo and i not in dias:
        dias.append(i)
        valor_abaixo.append(array[i])
    
for i in range(len(dias)):
    print(f"No dia {dias[i] + 1} o valor da venda ficou abaixa do esperado: {valor_abaixo[i]}")  