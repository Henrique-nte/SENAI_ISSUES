#Faça um programa que use a função valorPagamento para determinar o valor 
# a ser pago por uma prestação de uma conta. O programa deverá solicitar
#  ao usuário o valor da prestação e o número de dias em atraso e passar
#  estes valores para a função valorPagamento, que calculará o valor a 
# ser pago e devolverá este valor ao programa que a chamou. O programa
#  deverá então exibir o valor a ser pago na tela. Após a execução o
#  programa deverá voltar a pedir outro valor de prestação e assim continuar
#  até que seja informado um valor igual a zero para a prestação. Neste
#  momento o programa deverá ser encerrado, exibindo o relatório do dia,
#  que conterá a quantidade e o valor total de prestações pagas no dia.

def valorPagamento(valor, dias):

  if dias == 0:
    return valor
  
  if dias > 0:
      multa = valor * 0.03
      juros = valor * (0.01 * dias)
      return valor + multa + juros
  
quantidade = 0
soma = 0
while True:
  value = float(input("Valor da prestação: "))

  if value == 0:
    break
  quantidade += 1
  soma += value
  days = int(input("Dias em atraso: "))
  print(valorPagamento(value, days))

print("RELATÓRIO DO DIA\n")
print(f"Quantidade de prestações pagas no dia: {quantidade}")
print(f"Valor total de prestações: {soma}")
