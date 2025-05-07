#1- Crie um programa que receba como parâmetro um valor em reais e converta para
#dólares (Estados Unidos) ou yenes (Japão). Use um formatador de números apropriado
#para imprimir o resultado, levando o local em consideração. Se não tiver 
# como obter a cotação do dia, use R$ 1 = US$ 0,30 e R$ 1 = ¥ 30,00.
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

#1US$ = 5,71 R$
#1¥ = 0.04 R$
def converter(reais, opcao):
  cotacao_dolar = 0.17
  cotacao_yene = 24.95
  dolar = reais * cotacao_dolar
  yenes = reais * cotacao_yene
  if opcao == 1:
    print(f"{reais}R$ são: {dolar:.1f}US$")
  elif opcao == 2:
    print(f"{reais}R$ são: {yenes}¥")

while True:
  opcao = int(input("0 - SAIR\n1 - PARA CONVERTER PARA DOLAR\n2 - PARA CONVERTER PARA YENE\nOpção:"))
  if opcao == 0:
    break
  if opcao == 1:
    limpar()
    real = float(input("Real: "))
    converter(real, opcao)
    continue
  elif opcao == 2:
    limpar()
    real = float(input("Real: "))
    converter(real, opcao)
    continue
  else:
    limpar()
    print("Opção inválida!")
    continue