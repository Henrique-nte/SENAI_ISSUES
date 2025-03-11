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

for i in range (3):

    print(f"Para o vendedor {i + 1}")

    valor = int(input("Digite a quantidade de peças: "))
    pecas.append(valor)

    valor = int(input("Digite o preço da peça vendida: ")) 
    
     
    while valor in preco:
        
        novo_preco = int(input("Digite o preço novamente: ")) 
        preco.append(novo_preco)


    preco.append(valor)

    
for i in range(3):
    print(f"Para o vendedor {i + 1}")
    total_vendas = pecas[i] * preco[i]
    print(total_vendas)