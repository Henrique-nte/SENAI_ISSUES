#Data com mês por extenso. Construa uma função que receba uma data no
#formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso
#de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

meses = [
    'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
    'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
]

def devolver(data):
    if data < 8:
        print(None)
    else:
        dia = ''
        mes = ''
        ano = ''
        j = 0
        data = str(data)
        for i in data:
            if j > 1 and j <= 3:
                mes += i
            if j >= 0 and j < 2:
                dia += i
            if j > 3:
                ano += i
            j += 1
        mes = int(mes)
        mes -= 1
        return (f"{dia} de {meses[mes]} de {ano}")

data = int(input("Digite uma data: "))
print(devolver(data))