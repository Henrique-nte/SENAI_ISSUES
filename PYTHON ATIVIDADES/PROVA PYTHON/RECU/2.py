#2- Um professor registrou as notas de 35 alunos em uma prova. Faça um algoritmo que:

#●	Leia o nome e a nota de cada aluno.
#●	Informe a média geral da turma.
#●	Conte quantos alunos tiveram nota acima de 7.
soma_nota = 0
quantidade_maior_que_7 = 0

for i in range(35):

    #●	Leia o nome e a nota de cada aluno.
    nome = input(f"Nome do aluno {i + 1}: ")
    nota = int(input(f"Nota do aluno {i + 1}: "))

    soma_nota += nota

    #●	Conte quantos alunos tiveram nota acima de 7.
    if nota > 7:
        quantidade_maior_que_7 += 1

#●	Informe a média geral da turma.
media_geral = soma_nota / 35
print(f"Média geral da turma: {media_geral}")

print(f"Alunos com nota > 7: {quantidade_maior_que_7}")