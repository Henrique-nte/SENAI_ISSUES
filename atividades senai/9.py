#Na copa do mundo do Qatar, cada seleção tem uma lista oficial de 26 jogadores.
# Cada seleção prepara uma lista contendo o peso e a idade de cada um dos seus jogadores. 
# As 32 seleções que participam do torneio enviam essas listas para a FIFA. 
# Faça uma Programa que apresente as seguintes informações: 
#• peso médio e a idade média de cada um dos times; 
#• peso médio e a idade média de todos os participantes;
quantidade_jogadores = 0
soma_peso_total = 0
soma_idade_total = 0

for i in range(32):
    time = input(f"Nome do time {i + 1}: ")

    soma_peso = 0
    soma_idade = 0

    for j in range(26):
        peso_jogador = float(input(f"Peso do jogador {j + 1}: "))
        idade_jogador = int(input(f"Idade do jogador {j + 1}: "))

        soma_peso += peso_jogador
        soma_idade += idade_jogador
        soma_peso_total += peso_jogador
        soma_idade_total += idade_jogador

        quantidade_jogadores += 1

    # Cálculo correto das médias do time
    media_peso = soma_peso / 26
    media_idade = soma_idade / 26

    print(f"\nPara o time {time}:")
    print(f"Média do peso: {media_peso:.2f} kg")
    print(f"Média da idade: {media_idade:.2f} anos\n")

# Cálculo correto das médias gerais
media_peso_total = soma_peso_total / quantidade_jogadores
media_idade_total = soma_idade_total / quantidade_jogadores

print("Peso médio e idade média de todos os participantes:")
print(f"Média do peso: {media_peso_total:.2f} kg")
print(f"Média da idade: {media_idade_total:.2f} anos")
