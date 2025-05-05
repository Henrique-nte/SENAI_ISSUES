def nota_final(quatro, final):
    menor = quatro[0]
    soma_3 = 0
    for i in range(len(quatro)):
        if menor > quatro[i]:
            menor  = quatro[i]
        else:
            soma_3 += quatro[i]

    return soma_3 + final

def conceito(nota):
    if 90 <= nota <= 100:
        return 'A'
    elif 80 <= nota < 90:
        return 'B'
    elif 70 <= nota < 80:
        return 'C'
    elif 60 <= nota < 70:
        return 'D'
    elif 40 <= nota < 60:
        return 'E'
    elif 0 <= nota < 40:
        return 'F'
    else:
        return 'Nota inválida'

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

for aluno in alunos:
    numero = aluno[0]
    notas_mensais = aluno[1:5]
    prova_final = aluno[5]
    nota = nota_final(notas_mensais, prova_final)
    print(f"Aluno {numero} | Nota Final: {nota} | Conceito: {conceito(nota)}")