#Calculadora de IMC
#Solicite ao usuário seu peso e altura e calcule o IMC. 
#De acordo com o valor do IMC, classifique:
#Menor que 18.5: "Abaixo do peso"
#Entre 18.5 e 24.9: "Peso normal"
#Entre 25 e 29.9: "Sobrepeso"
#Maior que 30: "Obesidade"

while True:
  peso = float(input("Peso: "))
  altura = float(input("Altura: "))

  imc = peso / (altura ** 2)

  match imc:
    #Menor que 18.5: "Abaixo do peso"
    case imc if imc < 18.5:
      print("Abaixo do peso")
    #Entre 18.5 e 24.9: "Peso normal"
    case imc if imc >= 18.5 and imc <= 24.9:
      print("Peso normal")
    #Entre 25 e 29.9: "Sobrepeso"
    case imc if imc >= 25 and imc <= 29.9:
      print("Sobrepeso")
    #Maior que 30: "Obesidade"
    case imc if imc > 30:
      print("Obesidade")
