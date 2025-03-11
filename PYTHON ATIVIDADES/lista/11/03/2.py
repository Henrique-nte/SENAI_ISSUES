#2 - Determinada empresa vende 10 artigos diferentes. Para cada artigo, a empresa o identifica
# com um código numérico e o preço de venda. Faça um algoritmo para ler os 10 artigos e exibir 
#o código e o preço dos 3 artigos mais caros da empresa.

codigo_numerico = []
preco_venda = []
mais_caros = []
mais_caros_1 = 0
mais_caros_2 = 0
mais_caros_3 = 0

for i in range(4):

    valor = int(input("Digite o código numérico: "))
    codigo_numerico.append(valor)

    valor = int(input("Digite o preço: "))
    preco_venda.append(valor)

for i in range(4):

    if preco_venda[i] > mais_caros_1:
        mais_caros_1 = preco_venda[i]
        
for i in range(4):

    if preco_venda[i] < mais_caros_1 and preco_venda [i] > mais_caros_2:
        mais_caros_2 = preco_venda[i]

for i in range(4):
    if preco_venda[i] < mais_caros_1 and preco_venda[i] < mais_caros_2 and preco_venda[i] > mais_caros_3:
        mais_caros_3 = preco_venda[i] 

print(mais_caros_1)
print(mais_caros_2)
print(mais_caros_3)
       


