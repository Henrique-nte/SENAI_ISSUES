#Em uma classe há n alunos, cada um dos quais realizou k provas com pesos distintos. dados n, k
#os pesos das k provas e as notas de cada aluno, calcular a media ponderada das provas para cada 
#aluno ea media aritmetica da classe em cada uma das provas

alunos = 0
notas = []
media_ponderada = 0
media_aritmetica = 0
pesos = []
soma = 0
soma_notas = 0
for i in range(3):

    provas = int(input(f"Quantas provas o aluno {i + 1} realizou: "))

    for j in range(provas):
        valor = int(input(f"Nota para prova {j + 1}: "))
        notas.append(valor)

        valor2 = int(input(f"Peso da nota {j + 1}: "))
        pesos.append(valor2)
        
    soma += valor
    soma_notas += valor * valor2
    media_ponderada = soma_notas / soma
    media_aritmetica = soma / provas

    print(f"Para o aluno {i + 1}")
    print(f"Média ponderada: {media_ponderada}")
    print(f"Média aritmética: {media_aritmetica}")

#for i in range(3):
    

    