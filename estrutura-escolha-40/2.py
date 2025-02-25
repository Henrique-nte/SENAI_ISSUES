#---------------------------------------------------------------------------------------------------------------------------------------------
#Faça um programa que leia o seu peso na Terra e o número de um planeta e calcule qual será o seu peso neste planeta.
# A relação de planetas é:
#No 1 	Planeta	Gravidade Relativa


peso = float(input("Digite o seu peso: "))
print("1	Mercúrio	0,37")
print("2	Vênus	0,88")
print("3	Marte	0,38")
print("4	Júpiter	2,64")
print("5	Saturno	1,15")
print("6	Urano	1,17")

while True:
  escolha = int(input("Digite o número do planeta que você deseja: "))
  if (escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5 and escolha != 6):
      print("Número inválido.")
  if not (escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5 and escolha != 6):
    break

if escolha == 1:
    pesoplaneta = (peso / 10) * 0.37
    print("Em Mercúrio seu peso é: ", pesoplaneta)
elif escolha == 2:
    pesoplaneta = (peso / 10) * 0.88
    print("Em Vênus seu peso é: ", pesoplaneta)
elif escolha == 3:
    pesoplaneta = (peso / 10) * 0.38
    print("Em Marte seu peso é: ", pesoplaneta)
elif escolha == 4:
    pesoplaneta = (peso / 10) * 2.64
    print("Em Júpiter seu peso é: ", pesoplaneta)
elif escolha == 5:
    pesoplaneta = (peso / 10) * 1.15
    print("Em Saturno seu peso é: ", pesoplaneta)
elif escolha == 6:
    pesoplaneta = (peso / 10) * 1.17
    print("Em Urano seu peso é: ", pesoplaneta)


