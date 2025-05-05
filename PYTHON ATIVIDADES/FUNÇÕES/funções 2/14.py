def nota_final(quatro, final):
    menor = quatro[0]
    soma_3 = 0
    for i in range(len(quatro)):
        if menor > quatro[i]:
            menor  = quatro[i]
        else:
            soma_3 += quatro[i]

    return soma_3 + final

final_note = nota_final

def conceito(final_note):
    if 90 <= final_note <= 100:
        return 'A'
    elif 80 <= final_note < 90:
        return 'B'
    elif 70 <= final_note < 80:
        return 'C'
    elif 60 <= final_note < 70:
        return 'D'
    elif 40 <= final_note < 60:
        return 'E'
    elif 0 <= final_note < 40:
        return 'F'
    else:
        return 'Nota inválida'

print(conceito(final_note))

alunos = [
    [1, 7.0, 8.5, 6.5, 9.0, 8.0],
    [2, 5.5, 6.0, 7.0, 6.5, 7.5],
    [3, 9.0, 8.5, 9.5, 9.0, 9.5],
    [4, 4.0, 5.0, 4.5, 5.5, 6.0],
    [5, 6.5, 7.0, 6.0, 6.5, 7.0],
    [6, 8.0, 8.0, 8.0, 8.0, 8.0],
    [7, 3.5, 4.0, 4.5, 5.0, 5.5],
    [8, 10.0, 9.5, 10.0, 9.5, 8]
]

for i in range(len(alunos)):
    for j in range(1, len(alunos[0])):
        print(nota_final(alunos[j], alunos[j + 1], alunos[j + 2], alunos[j + 3], alunos[j + 4]))
    print(f"Para o aluno {i} Nota Final: {nota_final} Conceito: {conceito}")