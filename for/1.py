#1. Em uma eleição presidencial existem quatro candidatos. Os votos são informados através de códigos. Os dados utilizados para a contagem
# dos votos obedecem à seguinte codificação:
#- 1,2,3,4 = voto para os respectivos candidatos;
#- 5 = voto nulo;
#- 6 = voto em branco;
#Elabore um algoritmo que leia o código do candidato em um voto. Calcule e escreva:
#- total de votos para cada candidato;
#- total de votos nulos;
#- total de votos em branco;
#Como finalizador do conjunto de votos, tem-se o valor 0.

c1 = c2 = c3 = c4 = 0
nulo = 0
branco = 0

votantes = int(input("Votantes: "))
for i in range(votantes):
    votos = int(input("Digite o código para votar no candidato: "))
    if votos == 1:
        c1 += 1
    elif votos == 2:
        c2 += 1
    elif votos == 3:
        c3 += 1
    elif votos == 4:
        c4 += 1
    elif votos == 5:
        nulo += 1
    elif votos == 6:
        branco += 1

print("VOTOS CANDIDATO 1: ", c1)
print("VOTOS CANDIDATO 2: ", c2)
print("VOTOS CANDIDATO 3: ", c3)
print("VOTOS CANDIDATO 4: ", c4)
print("VOTOS NULO: ", nulo)
print("VOTOS BRANCO: ", branco)

