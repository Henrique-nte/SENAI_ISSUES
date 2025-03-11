#4- Dados dois vetores de tamanho N, diga se os mesmos possuem conteúdo igual.

vetor_1 = [2, 2, 3]
vetor_2 = [1, 2, 3]
contador = 0
for i in range(3):
    if vetor_1 [i] == vetor_2[i]:
        contador += 1

if contador == len(vetor_2):
    print("Sim")
else:
    print("Não")