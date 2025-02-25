#3-	Fazer um programa que retorne quantos valores digitados pelo usuário são negativos.
# Repetir o enquanto até o usuário digitar o valor ZERO:
contador = 0
while True: 
    numero = int(input("Digite um valor: "))
    if numero < 0:
        contador += 1

    if not (numero != 0):
        break

print("Quantidade de números negativos:", contador)