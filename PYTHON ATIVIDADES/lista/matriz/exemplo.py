matriz = []

for linha in range(4):
    linha = []
    for coluna in range(5):
        valor = float(input("Digite o valor da venda: "))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    print(matriz)

#printar matriz:
#for l,c in matriz: 
    #print(f"{l} | {c}")
    #para inteiros devemos tranformar em str = ex: str(c)