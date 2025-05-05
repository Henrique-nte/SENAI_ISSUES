#Desenvolva uma estrutura modular com as funções que:
#Calcula e retorna o Índice de Massa Corpórea (IMC) através da seguinte fórmula:
#IMC = PC / (Alt * Alt); onde: PC - Peso Corporal em kg e Alt- altura em metros.
#Recebe através de parâmetro o índice de massa corpórea e retorna à interpretação conforme a tabela a seguir:
#IMC				Interpretação
#-------------------------------------------
#Menos de 20		Magro
#20 – 24			Normal
#25 – 29			Acima do peso
#30 – 34			Obeso
#Acima de 34		Muito Obeso
#-------------------------------------------
def imc(peso, alt):
  imc = peso / (alt * alt)
  if imc < 20:
    print("Magro")
  elif imc >= 20 and imc <= 24:
    print("Normal")
  elif imc >= 25 and imc <= 29:
    print("Acima do peso")
  elif imc >= 30 and imc <= 34:
    print("Obeso")
  else:
    print("Muito Obeso")

massa = 70
alt = 170

imc(massa, alt)
  