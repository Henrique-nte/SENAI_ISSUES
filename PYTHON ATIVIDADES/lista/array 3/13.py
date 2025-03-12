#13 - Leia dois vetores de 20 posições e calcule um terceiro vetor contendo, nas posições
#pares os valores do
#primeiro e nas posições impares os valores do segundo.


vetor_1 = [45, 12, 78, 23, 56, 89, 34, 67, 90, 21, 54, 87, 32, 65, 98, 43, 76, 19, 52, 85]
vetor_2 = [10, 29, 63, 94, 17, 38, 72, 5, 81, 47, 13, 60, 24, 59, 83, 26, 71, 4, 91, 30]
vetor_3 = []

for i in range(20):
    if i % 2 == 1:  # Índice ímpar → Posição PAR (usa vetor_1)
        vetor_3.append(vetor_1[i])
    else:  # Índice par → Posição ÍMPAR (usa vetor_2)
        vetor_3.append(vetor_2[i])

print(vetor_3)