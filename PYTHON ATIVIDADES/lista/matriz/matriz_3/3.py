#3 - Crie um novo aplicativo, que simula a emissão de um relatório simplificado de folha de pagamento. O aplicativo deve utilizar
# diálogos de entrada de dados para solicitar o nome e o salário de cada funcionário.  O aplicativo deve permitir que você indique
# o número de funcionários que deseja registrar, desde que este número seja superior a zero. Se este diálogo for cancelado, 
#o aplicativo deve ser encerrado imediatamente.  
#Armazene os nomes dos funcionários em um vetor.  
#Utilize uma matriz que contenha quatro colunas para armazenar os seguintes dados de cada funcionário: 
#Salário bruto 
#INSS 
#Imposto de Renda 
#Salário líquido
#O nome e o salário bruto devem ser informados e os descontos devem ser calculados pelo aplicativo.  
#Se o nome ou o salário bruto não forem válidos, uma mensagem de erro deve ser exibida e o aplicativo deve solicitar novamente o dado.  
#As regras para a validação destes dados são as seguintes: 
#Nome: deve conter pelo menos 2 caracteres. 
#Salário: deve ser um valor igual ou superior a R$ 465,00.
#O teto para recolhimento de INSS é de RS 354,07. Esse é o valor máximo que pode ser descontado do funcionário. 
#Para cada funcionário, o aplicativo deve calcular os valores a serem descontados de seu salário a título de INSS e de Imposto de Renda. 
#Para calcular o valor do INSS a ser descontado, utilize a tabela abaixo: 
#Salário Alíquota Até R$ 965,67 8,0 
#De R$ 965,68 a R$ 1.609,45 9,0 
#De R$ 1.609,46 a R$ 3.218,90 11,0
#Para calcular o valor do Imposto de Renda, utilize a tabela abaixo. 
#Salário Alíquota Até R$ 1.434,00 0,0 
#De R$ 1.434,01 a R$ 2.150,00 7,5 
#De R$ 2.150,01 a R$ 2.886,00 15,0 
#De R$ 2.886,01 a R$ 3.582,00 22,5 
#Acima de 3.582,00 27,5
#O aplicativo também deve calcular o salário líquido a ser pago a cada funcionário, que representa o valor do 
#salário decrescido dos valores do INSS e do Imposto de Renda.  Quando você cancelar um dos diálogos de entrada de
# dados, este aplicativo deve exibir uma mensagem contendo o resumo da folha de pagamento.  
#Este resumo deve ter o nome e o salário bruto de cada funcionário registrado, os valores do INSS e do Imposto de
# Renda que serão descontados e o salário líquido a ser pago.  
#Ao final deste resumo, devem ser indicadas algumas totalizações: 
#A soma do valor de todos os salários brutos 
#A soma dos descontos de INSS 
#A soma dos descontos de Imposto de Renda 
#A soma de todos os salários líquidos



#3 - Crie um novo aplicativo, que simula a emissão de um relatório simplificado de folha de pagamento. O aplicativo deve utilizar
# diálogos de entrada de dados para solicitar o nome e o salário de cada funcionário.  O aplicativo deve permitir que você indique
# o número de funcionários que deseja registrar, desde que este número seja superior a zero. Se este diálogo for cancelado, 
#o aplicativo deve ser encerrado imediatamente.  
#Armazene os nomes dos funcionários em um vetor.  
n = int(input("Quantos Funcionários deseja registrar?"))
funcionarios = []
contador = 0
if n > 0:
    for linha in range(n):
        nome = str(input("Nome do funcionário: "))
        for caractere in nome:
            contador += 1
        if contador > 2:
            funcionarios.append([nome])
        else:
            print("Nome inválido")


#Utilize uma matriz que contenha quatro colunas para armazenar os 
#seguintes dados de cada funcionário: 
#Salário bruto 
#INSS 
#Imposto de Renda 
#Salário líquido
#O nome e o salário bruto devem ser informados e os descontos devem ser calculados pelo aplicativo.  
#Se o nome ou o salário bruto não forem válidos, uma mensagem de erro deve ser exibida e o aplicativo deve solicitar novamente o dado.  
#As regras para a validação destes dados são as seguintes: 
#Nome: deve conter pelo menos 2 caracteres. 
#Salário: deve ser um valor igual ou superior a R$ 465,00.
#O teto para recolhimento de INSS é de RS 354,07. Esse é o valor máximo que pode ser descontado do funcionário. 
#Para cada funcionário, o aplicativo deve calcular os valores a serem descontados de seu salário a título de INSS e de Imposto de Renda. 
#Para calcular o valor do INSS a ser descontado, utilize a tabela abaixo: 
#Salário Alíquota Até R$ 965,67 8,0 
#De R$ 965,68 a R$ 1.609,45 9,0 
#De R$ 1.609,46 a R$ 3.218,90 11,0
#Para calcular o valor do Imposto de Renda, utilize a tabela abaixo. 
#Salário Alíquota Até R$ 1.434,00 0,0 
#De R$ 1.434,01 a R$ 2.150,00 7,5 
#De R$ 2.150,01 a R$ 2.886,00 15,0 
#De R$ 2.886,01 a R$ 3.582,00 22,5 
#Acima de 3.582,00 27,5
#O aplicativo também deve calcular o salário líquido a ser pago a cada funcionário, que representa o valor do 
#salário decrescido dos valores do INSS e do Imposto de Renda.
dados = []
soma_brutos = 0
i= 0
inss = 0
for linha in range(len(funcionarios)):
    linha = []
    nome = funcionarios[i] #Pega o nome da lista de funcionários
    linha.append(nome)
    for coluna in range(1):
        bruto = float(input("Salário Bruto: "))
        linha.append(bruto)

        inss_calculo = 0.0
        soma_des_inss = 0
        #Calculo do INSS
        if bruto <= 965.67:
            inss = "8%"
            inss_calculo = bruto * 0.08
            
        elif bruto > 965.68 and bruto <= 1609.45:
            inss = "9%"
            inss_calculo = bruto * 0.09
            
        elif bruto > 1609.46 and bruto < 3218.90:
            inss = "11%"
            inss_calculo = bruto * 0.11
            
        if inss_calculo < 354.07:
            liquido = bruto - inss_calculo
        else:
            print("Teto atingido")
            liquido = bruto - 354.07

        #Calculo do imposto de renda
        #Salário Alíquota Até R$ 1.434,00 0,0 
        #De R$ 1.434,01 a R$ 2.150,00 7,5 
        #De R$ 2.150,01 a R$ 2.886,00 15,0 
        #De R$ 2.886,01 a R$ 3.582,00 22,5 
        #Acima de 3.582,00 27,5
        
        imposto_renda = 0.0  
        soma_liquido = 0
        soma_imposto_renda = 0
        if bruto < 1434.00:
            liquido = bruto
        elif bruto > 1434.01 and bruto <= 2150:
            imposto_renda = bruto * 0.075
            liquido -= imposto_renda
        elif bruto > 2151 and bruto <= 2886:
            imposto_renda = bruto * 0.15
            liquido -= imposto_renda
        elif bruto > 2887 and bruto <= 3582:
            imposto_renda = bruto * 0.225
            liquido -= imposto_renda
        elif bruto > 3582:
            imposto_renda = bruto * 0.275
            liquido -= imposto_renda

        #A soma do valor de todos os salários brutos
        soma_brutos += bruto 
        #A soma dos descontos de INSS
        soma_des_inss += inss_calculo
        #A soma dos descontos de Imposto de Renda 
        soma_imposto_renda += imposto_renda
        #A soma de todos os salários líquidos
        soma_liquido += liquido  

        taxa_inss = inss
        linha.append(taxa_inss)
        valor = imposto_renda
        linha.append(valor)
        liquido = bruto - inss_calculo
        linha.append(liquido)
        i += 1
    dados.append(linha)

#print("|Funcionário|Salário Bruto|INSS|Imposto de Renda|Salário Líquido|")
#for linha in dados:
    #for elemento in linha:
        #print(elemento,"|    ", end = "")
    #print()

#Ao final deste resumo, devem ser indicadas algumas totalizações:
 
#A soma do valor de todos os salários brutos
print(f"Soma dos salários brutos: {soma_brutos}")
#A soma dos descontos de INSS 
print(f"Soma dos descontos de INSS: {soma_des_inss}")
#A soma dos descontos de Imposto de Renda 
print(f"Soma descontos de Imposto de Renda: {soma_imposto_renda}")
#A soma de todos os salários líquidos
print(f"Soma dos salários liquidos: {soma_liquido}")