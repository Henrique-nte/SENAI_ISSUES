#13 - Leia dois vetores de 20 posições e calcule um terceiro vetor contendo, nas posições
#pares os valores do
#primeiro e nas posições impares os valores do segundo.

vetor_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

vetor_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

vetor_3 = []

for i in range(20):
    if vetor_1[i] % 2 == 0:
        vetor_3.append(vetor_1[i])

print()

for i in range(20):
    if vetor_2[i] % 2 != 0:
        vetor_3.append(vetor_2[i])

print(vetor_3)