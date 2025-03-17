#13 - Leia dois vetores de 20 posições e calcule um terceiro vetor contendo, nas posições
#pares os valores do
#primeiro e nas posições impares os valores do segundo.


vetor_1 = [1, 2, 3, 4, 5]
vetor_2 = [9, 8, 7, 6, 5]
vetor_3 = []

for i in range(len(vetor_1)):
    if i % 2 == 1:  # Índice ímpar → Posição PAR (usa vetor_1)
        vetor_3.append(vetor_1[i])
    else:  # Índice par → Posição ÍMPAR (usa vetor_2)
        vetor_3.append(vetor_2[i])

print(vetor_3)