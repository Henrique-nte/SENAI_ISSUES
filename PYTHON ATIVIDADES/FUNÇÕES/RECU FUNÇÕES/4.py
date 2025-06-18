#Crie uma função que recebe três números inteiro representando horas, minutos e
#segundos e converte esse valor para segundos

def converter(horas, minutos, segundos):
    total = (horas * 3600) + (minutos * 60) + segundos
    return total

one = 2
two = 25
three = 30

print(converter(one, two, three))