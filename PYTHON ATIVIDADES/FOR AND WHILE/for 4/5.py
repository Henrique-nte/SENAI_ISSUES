#Uma loja utiliza o código 1 para transação à vista e 2 para transação a prazo. 
#Faça um programa que receba o código e o valor de 15 transações. Calcule e mostre: 

#O valor total das compras à vista
#O valor total as compras a prazo
#O valor total das compras efetuadas
#O valor da primeira prestação das compras a prazo, sabendo se que essas serão pagas em três vezes

total_vista = 0
total_prazo = 0
total_geral = 0
primeira_prestacao = 0

for i in range(15):
    valor = int(input("Digite valor da compra: "))

    print("Digite 1 para transação à vista\nDigite 2 para transação à prazo")
    codigo = int(input(":"))
    total_geral += valor

    if codigo == 1:
            total_vista += valor
    elif codigo == 2:
          total_prazo += valor

if total_prazo > 0:
      primeira_prestacao = total_prazo / 3


#O valor total das compras à vista
print(f"Valor total das compras à vista: {total_vista}")
#O valor total as compras a prazo
print(f"Total compras a prazo: {total_prazo}")
#O valor total das compras efetuadas
print(f"Valor total das compras efetuadas: {total_geral}")
#O valor da primeira prestação das compras a prazo, sabendo se que essas serão pagas em três vezes
print(f"Valor da primeira prestação: {primeira_prestacao}")