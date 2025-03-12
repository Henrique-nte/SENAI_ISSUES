#5- Faça um programa que receba a quantidade de peças vendidas 
#por vendedor e armazene essas quantidades
#em um vetor. Receba também o preço da peça vendida de cada vendedor
# e armazene esses preços em outro vetor. Existem apenas dez vendedores
# e cada vendedor pode vender apenas um tipo de peça, isto é, para cada
# vendedor existe apenas um preço. Calcule e mostre a quantidade total
# de peças vendidas por todos os vendedores e para cada vendedor calcule
# e mostre o valor total da venda, isto é, a quantidade de peças * o preço da peça.

pecas = []
preco = []
valores = []
#vendedor = []
novo_preco = 0
i = 0
soma_pecas =0
for i in range(3):
    print(f"Vendedor {i + 1}")

    valor = float(input("Quantidade de peças: "))
    pecas.append(valor)
    soma_pecas += valor

    while True:
        valor = float(input("Preço da peça vendida: ")) 
        
        if valor in preco:
            print("Erro. Preço repetido")
            continue
        if preco != valor:
            preco.append(valor)
            break
    
    print(f"Para o vendedor {i + 1} Preço: {preco[i]}")
    

for i in range(3):
    print(f"Para o vendedor {i + 1}")
    total_vendas = pecas[i] * preco[i]
    print(total_vendas)
print(f"Quantidade total de peças: {soma_pecas}")