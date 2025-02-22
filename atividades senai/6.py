# 6 - Peça ao usuário para fornecer um número inicial e um intervalo.
# Em seguida, faça uma contagem regressiva do número inicial até zero,
# decrementando pelo intervalo especificado.

numero = int(input("Número inicial: "))
intervalo = int(input("Intervalo: "))

if intervalo <= 0:
    print("O intervalo deve ser um número positivo.")
else:
    while numero >= 0:
        print(numero)
        numero -= intervalo

        