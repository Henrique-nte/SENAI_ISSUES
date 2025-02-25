#9.	Crie um programa que calcule o desconto a ser aplicado em uma compra. 
#O usuário deve informar o valor total da compra e o tipo de cliente 
#(Regular, VIP ou Funcionário). As regras para o desconto são:
#●	Regular: 0% de desconto
#●	VIP: 10% de desconto
#●	Funcionário: 20% de desconto

valor = float(input("Valor total: "))
tipo = (input("Tipo de cliente: ")).lower()
total = 0
desconto = 0
match tipo:
    case 'funcionario':
        desconto = valor * 0.20
    case 'vip':
        desconto = valor * 0.10
    case 'regular':
        desconto = 0
    case _:
        print("Tipo inválido.")

if desconto == 0:
    print("Sem desconto.")
    print(f"Valor total a pagar: {valor} ")
elif desconto != 0:
    total = valor - desconto
    print(f"Para o tipo {tipo} o desconto é: {desconto}")
    print(f"Valor total a pagar: {total} ")
