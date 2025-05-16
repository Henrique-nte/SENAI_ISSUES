#Desenvolva uma função que receba um array com os valores de faturamento mensal
#(3 meses) de diferentes
#filiais e retorne o faturamento total de cada filial em um novo array.
#● No programa principal, peça ao usuário que insira os dados de faturamento
#trimestral de 3 filiais e
#exiba o total de cada uma utilizando a função.

def faturamento(array):
    dados = []
    for i in range(len(array)):
        faturamento = 0.0
        for j in range(len(array)):
            faturamento += array[i][j]
        dados.append(faturamento)
    return dados

data = []

for i in range(3):
    linha = []
    print(f"Filial {i + 1}")
    for coluna in range(3):
        valor = float(input(f"Mês {coluna + 1}: "))
        linha.append(valor)
    data.append(linha)

i = 0
for filial in faturamento(data):
    print(f"Faturamento Filial {i + 1}: {filial}R$")
    i += 1