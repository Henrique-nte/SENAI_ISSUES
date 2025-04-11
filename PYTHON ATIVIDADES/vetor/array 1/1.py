#1- Faça um programa em JS que receba o total das vendas de cada vendedor e 
#armazenadas em um vetor. Receba também o percentual de comissão de cada vendedor 
#e armazene-os em outro vetor. Receba os nomes desses vendedores e armazene ­os em um 
#terceiro vetor. Existem apenas dez vendedores. Calcule e mostre: 

#a) Um relatório com os nomes dos vendedores e os valores a receber; 
#c) O maior valor a receber e quem o receberá; 
#d) O menor valor a receber e quem o receberá.

nomes = []
vendas = []
percentual = []
comissao = []

comissao_maior = [float('-inf')]  # Inicia com o valor mínimo possível
nome_maior = [None]  

comissao_menor = [float('inf')]  # Inicia com o valor máximo possível
nome_menor = [None]  

for i in range(2):
    
    valor = input("Digite um nome: ")
    nomes.append(valor)

    valor = int(input("Digite o total de vendas: "))
    vendas.append(valor)

    valor = float(input("Digite um percentual de comissão: "))
    percentual.append(valor)

    valor = (percentual[i] * vendas[i]) / 100
    comissao.append(valor)

    if comissao[i] > comissao_maior[0]:
        comissao_maior[0] = comissao[i]
        nome_maior[0] = nomes[i]

    if comissao[i] < comissao_menor[0]:
        comissao_menor[0] = comissao[i]
        nome_menor[0] = nomes[i]


#a) Um relatório com os nomes dos vendedores e os valores a receber; 
print("RELATÓRIO\n")

for i in range(2):
    print(f"{nomes[i]} receberá: {comissao[i]}")


#c) O maior valor a receber e quem o receberá; 
print(f"Maior valor a receber: {comissao_maior[0]}, quem irá receber: {nome_maior[0]} ")
#d) O menor valor a receber e quem o receberá.
print(f"Menor valor a receber: {comissao_menor[0]}, quem irá receber: {nome_menor[0]} ")