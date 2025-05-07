#4-• Sortear um número de 0 a 1000 (dica: usar random)
#• Pedir um palpite ao usuário. Se ele errar, informar se o palpite é maior ou
#menor do que o número sorteado.
#• Pedir novos palpites até que o usuário acerte e, depois disso, mostrar em
#quantas tentativas ele acertou.

import random
numero_aleatorio = random.randint(0, 1000)
print(numero_aleatorio)

def avaliar(palpite, number_aleatorio):
  if palpite == number_aleatorio:
    print(f"Você acertou na {i + 1}° tentativa")
    return True
  
def dica(palpite):
  if palpite < numero_aleatorio:
    print("Dica: O número é maior que isso")
  if palpite > numero_aleatorio:
    print("Dica: O número é menor que isso")


i = 0
while True:
  palpite = int(input("Digite um palpite: "))
  resposta = avaliar(palpite, numero_aleatorio)
  if resposta == True:
    break
  i += 1
  dica(palpite)