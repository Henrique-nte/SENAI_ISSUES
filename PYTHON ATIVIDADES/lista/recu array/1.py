#1- Crie um programa que leia o peso de 8 pessoas. Mostre quantas estão abaixo de
# 60 kg, entre 60 kg e 80 kg e acima de 80 kg.
pesos = []
abaixo = 0
for i in range(8):
    peso = int(input("Pesos"))
    pesos.append(peso)

for i in range(len(pesos)):
    if pesos[i] < 60:
        abaixo += 1