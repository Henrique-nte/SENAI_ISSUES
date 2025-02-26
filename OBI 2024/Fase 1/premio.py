paes = int(input("Número de pães vendidos na semana: "))
doces = int(input("Número de doces vendidos na semana: "))
bolos = int(input("Número de bolos vendidos na semana: "))

ponto_paes = paes 
ponto_doces = doces * 2
ponto_bolos = bolos * 3

soma = ponto_paes + ponto_doces + ponto_bolos

if soma >= 150:
    print("B")
elif soma >= 120 and soma < 150:
    print("D")
elif soma >= 100 and soma < 120:
    print("P")
elif soma < 100:
    print("N")
