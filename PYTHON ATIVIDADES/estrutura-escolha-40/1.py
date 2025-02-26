#As vendas parceladas se tornaram uma ótima opção para os lojistas, que a cada dia
#criam novas promoções para tentar conquistar novos clientes.
#Faça um programa onde o lojista possa entrar com o preço do produto e receba as seguintes informações:
#O valor com 10% de desconto para pagamento à vista
#O valor da prestação para parcelamento sem juros, em 5x
#O valor da prestação para parcelamento com juros, em 10x, com 20% de acréscimo no valor do 1 produto.
valor = float(input("Digite o valor do produto:"))

escolha = input("Pagamento à vista?").upper()
if escolha == "SIM":
    desconto = valor * 0.10
    total = valor - desconto
    print("Valor com 10% de desconto: ", total)

elif escolha == "NÃO" or escolha == "NAO":
    totalparce = valor / 5
    print("Valor da prestação para parcelamento sem juros, em 5x: ", totalparce)
    juros = (valor * 0.20)
    totalparce = (valor + juros) / 10
    print("O valor da prestação para parcelamento com juros, em 10x, com 20% de acréscimo no valor do 1 produto: ", totalparce)