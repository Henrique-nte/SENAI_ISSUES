#Solicite ao usuário o valor do capital inicial,
# a taxa de juros mensal e o tempo de aplicação.
# Calcule o valor final utilizando a fórmula de juros compostos.

capital = float(input("Capital: "))
taxa = float(input("Taxa de juros mensal: ")) / 100
tempo = float(input("Tempo de aplicação: "))
#M = C ( 1+i)t

montante = capital * (1 + taxa) ** tempo

print("Montante: ", montante)

