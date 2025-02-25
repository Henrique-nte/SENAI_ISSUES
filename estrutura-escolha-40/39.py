#Solicite ao usuário o número de votos para três candidatos e determine
# qual candidato obteve a maior quantidade de votos, considerando que pode haver empate.

candidato1 = int(input("Digite a quantidade de votos para o candidato 1: "))
candidato2 = int(input("Digite a quantidade de votos para o candidato 2: "))
candidato3 = int(input("Digite a quantidade de votos para o candidato 3: "))

if candidato1 == candidato2 and candidato2 == candidato3:
    print("EMPATE!")

elif candidato1 > candidato2:
    if candidato1 > candidato3:
        print("Candidato 1 é o vencedor!")

elif candidato2 > candidato1:
    if candidato2 > candidato3:
        print("Candidato 2 é o vencedor!")

elif candidato3 > candidato2:
    if candidato3 > candidato1:
        print("Candidato 3 é o vencedor!")

