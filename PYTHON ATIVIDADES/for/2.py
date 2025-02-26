#A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
#coletando dados sobre o número de filhos e salário. A prefeitura deseja saber:
#a) média do salário da população;
#b) média do número de filhos;
#) maior salário;
#d) percentual de pessoas com salário até R$100,00.
#O final da leitura de dados se dará com a entrada de um salário negativo.


pessoas = int(input("Qual a quantidade de pessoas da pesquisa?: "))
media = 0
mediafilhos = 0
maior = 0
ate100 = 0
soma = 0
somafilhos = 0
percentual = 0

for i in range(pessoas):
    filhos = int(input("Número de filhos: "))
    salario = int(input("Salário: "))
    if salario > 0:
        soma += salario
        media = soma / pessoas
        somafilhos += filhos
        mediafilhos = somafilhos / pessoas
        if salario <= 100:
            ate100 += 1

        percentual = (ate100 / pessoas) * 100

        if salario > maior:
            maior = salario
    else:
        print("Salário negativo.")
        break

print("Média do salário da população: ", media)
print("Média do número de filhos: ", mediafilhos)
print("Maior salário: ", maior)
print("Ate 100: ", percentual)


