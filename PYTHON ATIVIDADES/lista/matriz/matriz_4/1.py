#1- Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
#As perguntas são: Telefonou para a vítima?; Esteve no local do crime?; Mora perto da vítima?;
#Devia para a vítima?; Já trabalhou com a vítima? O programa deve no final emitir uma classificação
#sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
#eve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
#contrário, ele será classificado como "Inocente".

contador = 0
print("1 - SIM")
print("2 - NÃO")
 
primeira = input("Telefonou para a vítima?")
if primeira == 1:
    contador += 1
segunda = input("Estava no local do crime?")
if segunda == 1:
    contador += 1
terceira = input("Mora perto da vítima?")
if terceira == 1:
    contador += 1
quarta = input("Devia para a vítima?")
if quarta == 1:
    contador += 1
quinta = input("Já trabalhou com a vítima?")


if contador == 0:
    clasificacao = "Inocente"
if contador == 2:
    clasificacao = "Suspeito"
if contador >= 3 and contador <= 4:
    clasificacao = "Inocente"
if contador == 0:
    clasificacao = "Inocente"
