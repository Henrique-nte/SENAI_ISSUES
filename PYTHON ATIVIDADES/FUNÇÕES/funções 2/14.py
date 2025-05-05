# Questão 14 - Avaliação de aproveitamento de uma disciplina

# A disciplina tem 4 provas mensais, cada uma valendo 20 pontos
# e uma prova final que vale 40 pontos.

# A nota final do aluno será a soma:
# - das 3 maiores notas entre as 4 provas mensais
# - com a nota da prova final

# A classificação final (conceito) segue essa tabela:


# Objetivo:
# Criar uma sub-rotina (função) que:
# - Recebe como entrada 4 números inteiros (as notas das provas mensais)
# - Retorna a soma das 3 maiores entre essas 4 notas

def nota_final(quatro, final):
    menor = quatro[0]
    soma_3 = 0
    for i in range(len(quatro)):
        if menor > quatro[i]:
            menor  = quatro[i]
        else:
            soma_3 += quatro[i]

    return soma_3 + final

quatro = [7, 8, 6, 9]
final = 8
print(nota_final(quatro, final))

final_note = nota_final
# De 90 a 100 - Conceito A
# De 80 a 89  - Conceito B
# De 70 a 79  - Conceito C
# De 60 a 69  - Conceito D
# De 40 a 59  - Conceito E
# De 0  a 39  - Conceito F

def conceito(nota_final):

# Depois, criar um algoritmo principal que:
# ● Leia os dados de 80 alunos.
#   - Cada linha contém: número do aluno, 4 notas mensais, 1 nota da prova final

# ● Para cada aluno:
#   - Use a sub-rotina para calcular a soma das 3 maiores provas mensais
#   - Some com a nota da prova final → isso é a nota final

# ● Verifique qual é o conceito correspondente à nota final

# ● Exiba para cada aluno:
#   - Número do aluno
#   - Nota final
#   - Conceito

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
# ● Para cada aluno:
#   - Use a sub-rotina para calcular a soma das 3 maiores provas mensais
#   - Some com a nota da prova final → isso é a nota final

# ● Verifique qual é o conceito correspondente à nota final

# ● Exiba para cada aluno:
#   - Número do aluno
#   - Nota final
#   - Conceito

for i in range(len(alunos)):
    for j in range(1, len(alunos[0])):
        print(nota_final(alunos[j], alunos[j + 1], alunos[j + 2], alunos[j + 3], alunos[j + 4]))
    print(f"Para o aluno {i} Nota Final: {nota_final} Conceito: {conceito}")