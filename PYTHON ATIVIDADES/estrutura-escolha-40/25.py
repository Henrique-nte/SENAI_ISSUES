#Escolher a categoria de um produto
#O usuário deve informar o valor de um produto e o programa
#deve retornar a categoria do produto de acordo com a tabela:
#Menor que 50: "Econômico"
#Entre 50 e 150: "Médio"
#Maior que 150: "Premium"

valor = float(input("Valor do produto: "))

match valor:
  case valor if valor < 50:
    print("Econômico")
  case valor if valor >= 50 and valor <=150:
    print("Médio")
  case valor if valor > 150:
    print("Premium")
  

  