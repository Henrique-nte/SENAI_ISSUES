#Duas amigas estão na fila para comprar ingressos para uma sessão de cinema. O preço dos ingressos,
#em Reais, é dado na tabela abaixo:
#Idade Preço
#até 17 anos 15
#18 a 59 anos 30
#60 anos ou mais 20
#Dadas as idades das amigas, escreva um programa para calcular o total a ser pago pelos dois
#ingressos.
#Entrada
#A entrada contém duas linhas, cada linha contendo um inteiro, a idade de uma das amigas.
#Saída
#Seu programa deve produzir uma única linha, contendo um único inteiro, que deve ser o valor total
#em Reais a ser pago pelos dois ingressos.
#Restrições
#• 1 ≤ idade ≤ 100
soma_precos = 0
i = 0
while i < 2:
    idade = int(input("Digite uma idade: "))
    #até 17 anos 15
    if idade <= 17:
        preco = 15
    #18 a 59 anos 30
    elif idade >= 18 and idade <= 59:
        preco = 30
    #60 anos ou mais 20
    elif idade >= 60:
        preco = 20
    i += 1
    
    soma_precos += preco

print(f"Total: {soma_precos}")



