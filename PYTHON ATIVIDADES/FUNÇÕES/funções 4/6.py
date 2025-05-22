#Data com mês por extenso. Construa uma função que receba uma data no
#formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso
#de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

meses = [
    'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
    'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
]

def devolver(data):
    if data < 8:
        return None
    elif data >= 8:
        #Pegar Dia
        dia = data // 1000000

        #Pegar Mês
        numeros = []
        date = str(data)
        for i in range(len(date)):
            numeros.append(date[i])
        
        mes = numeros[3]
        mes = int(mes)
        
        #Pegar Ano
        ano = data %10000
        
        return (f"{dia} de {meses[mes - 1]} de {ano}")

#data = int(input("Digite uma data: "))
data = 3333
print(devolver(data))