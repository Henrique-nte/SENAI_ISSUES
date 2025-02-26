#4-	A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, 
#coletando dados sobre o número de filhos e salário. A prefeitura deseja saber:   
#a) média do salário da população; 
#b) média do número de filhos; 
#c) maior salário; 
#d) percentual de pessoas com salário até R$100,00. 
#O final da leitura de dados se dará com a entrada de um salário negativo.  

ate100 = 0
soma_filhos = 0
contador = 0
soma_salarios = 0
maior_salario = 0
escolha = 0
percentual_100 = 0

while True:

    numero_filhos = int(input("Número de filhos: "))
    soma_filhos += numero_filhos
    salario = int(input("Salário: "))
    if salario < 0:
        break
    soma_salarios += salario
    contador += 1
    #a) média do salário da população; 
    media_salario = soma_salarios / contador
    #b) média do número de filhos;
    media_filhos = soma_filhos / contador
    #c) maior salário;
    if salario > maior_salario:
        maior_salario = salario
    #d) percentual de pessoas com salário até R$100,00. 
    if salario <= 100:
        ate100 += 1
    percentual_100 =  (ate100 * 100) / contador

    escolha = int(input("(0) PARA PARAR e (1) PARA CONTINUAR: "))
    if escolha == 1:
        continue
    elif escolha == 0:
        print(media_salario)
        print(media_filhos)
        print(maior_salario)
        print(percentual_100)   
        break


