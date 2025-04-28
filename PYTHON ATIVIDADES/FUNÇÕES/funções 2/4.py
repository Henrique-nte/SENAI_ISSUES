# 4 - Desenvolva uma estrutura modular com uma função que recebe através 
# de parâmetro um número inteiro positivo e retorna à quantidade 
# de dígitos deste número.

def verificador(inteiro):
  digitos = 0
  for i in inteiro:
    digitos += 1
  
  return digitos

numero = 12
if numero > 0:
  print(verificador(str(numero)))