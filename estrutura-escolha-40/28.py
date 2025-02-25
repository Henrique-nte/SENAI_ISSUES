#Escolher entre dois tipos de desconto
#Solicite o valor de uma compra e, dependendo do valor, 
#ofereça um dos dois tipos de desconto:
#Menor que 100: "Desconto de 5%"
#Maior ou igual a 100: "Desconto de 10%"

valor = float(input("Valor da compra: "))

match valor:
  case valor if valor < 100:
    desconto = valor * 0.05
  case valor if valor >= 100:
    desconto = valor * 0.10

total = valor - desconto
print(f"Desconto: {desconto}")
print(f"Valor total: {total}")