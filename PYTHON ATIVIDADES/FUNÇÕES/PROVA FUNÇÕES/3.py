#Desenvolva uma função que receba como parâmetros o custo de produção
# de um produto e seu preço de
#venda. A função deve retornar o valor do lucro e a margem de lucro percentual.
#● 3 produtos fornecidos pelo usuário.

def lucro(custo, preco):
    lucro = preco - custo
    if lucro < 0:
        lucro = 0
    percentual = (custo / 100) * lucro
    return f"Lucro: {lucro}R$\npercentual de lucro: {percentual}%"

for i in range(3):
    custo = float(input(f"Custo do produto {i + 1}:"))
    preco = float(input(f"Preço do produto {i + 1}:"))
    print(f"Para o produto {i + 1}")
    print(lucro(custo, preco))