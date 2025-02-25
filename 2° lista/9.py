#Crie um programa de adivinhação em que o computador escolhe 
# aleatoriamente um número entre 1 e 50, e o usuário precisa adivinhar. 
# O programa deve fornecer feedback (maior ou menor) a cada tentativa e 
# permitir apenas 5 tentativas para acertar. Se o usuário acertar antes
# do limite, exiba uma mensagem de vitória; caso contrário, revele o número ao final.

import random
i = 1
numero_aleatorio = random.randint(1, 50)
#print(numero_aleatorio)

while i <= 5:
  
  tentativa = int(input("Tente adivinhar um número entre 1 a 50: "))
  if tentativa == numero_aleatorio:
    print(f"Parabéns você acertou na {i}° tentativa!")
    break
  elif tentativa < numero_aleatorio:
    print("O número é maior que isso!")
  elif tentativa > numero_aleatorio:
    print("O número é menor que isso!")
  i += 1
  
if tentativa != numero_aleatorio:
  print("Não foi dessa vez, acabaram suas tentaivas.")
  print(f"O número era {numero_aleatorio}")
  


