#2- Faça um programa que percorre uma lista com o seguinte
#formato: [['Brasil', 'Itália', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Itália',
#'Espanha', [7,8]]]. Essa lista indica o número de faltas que cada time fez em
#cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10
#faltas e a Itália fez 9. O programa deve imprimir na tela: a) o total de faltas
#do campeonato b) o time que fez mais faltas c) o time que fez menos faltas.
matriz = [
    ['Brasil', 'Itália', [1, 5]],
    ['Brasil', 'Espanha', [2, 5]],
    ['Itália', 'Espanha', [3, 5]]
]

times = []
faltas = []

# Coleta os times
for jogo in matriz:
    if jogo[0] not in times:
        times.append(jogo[0])
    if jogo[1] not in times:
        times.append(jogo[1])

# Inicializa a contagem de faltas
for _ in range(len(times)):
    faltas.append(0)

print(faltas)

# Soma as faltas por time e total
total_faltas = 0

for jogo in matriz:
    time1 = jogo[0]
    time2 = jogo[1]
    f1 = jogo[2][0]
    f2 = jogo[2][1]

    total_faltas += f1 + f2

    for i in range(len(times)):
        if times[i] == time1:
            faltas[i] += f1
        if times[i] == time2:
            faltas[i] += f2

# Determina quem fez mais e menos faltas
mais_faltas = faltas[0]
menos_faltas = faltas[0]
time_mais = times[0]
time_menos = times[0]

for i in range(1, len(times)):
    if faltas[i] > mais_faltas:
        mais_faltas = faltas[i]
        time_mais = times[i]
    if faltas[i] < menos_faltas:
        menos_faltas = faltas[i]
        time_menos = times[i]

# Resultados
print("Total de faltas no campeonato:", total_faltas)
print("Time que fez mais faltas:", time_mais, f"({mais_faltas})")
print("Time que fez menos faltas:", time_menos, f"({menos_faltas})")
