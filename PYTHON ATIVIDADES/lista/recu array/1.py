#1- Crie um programa que leia o peso de 8 pessoas. Mostre quantas estão abaixo de
# 60 kg, entre 60 kg e 80 kg e acima de 80 kg.
pesos = []
abaixo = 0
entre = 0
acima = 0

for i in range(8):
    peso = int(input("Peso: "))
    pesos.append(peso)

for i in range(len(pesos)):
    if pesos[i] < 60:
        abaixo += 1
    elif pesos[i] >= 60 and pesos[i] <= 80:
        entre += 1
    elif pesos[i] > 80:
        acima += 1

print(f"Pessoas abaixo: {abaixo}")
print(f"Pessoas entre: {entre}")
print(f"Pessoas acima: {acima}")