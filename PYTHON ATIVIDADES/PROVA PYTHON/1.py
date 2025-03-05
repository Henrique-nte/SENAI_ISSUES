#1.	Uma universidade deseja fazer um levantamento a respeito do seu concurso vestibular. 
#Para cada curso, é fornecido o seguinte conjunto de valores:  o código do curso;  o número de vagas;  
#número de candidatos do sexo masculino;  número de candidatos do sexo feminino. O último conjunto, 
#para indicar fim de dados, contém o código do curso igual a zero. Fazer um algoritmo que: 
#a.	 calcule e escreva, para cada curso, o número de candidatos por vaga e a porcentagem de 
#candidatos do sexo feminino (escreva também o código correspondente do curso);  
#b.	determine o maior número de candidatos por vaga e escreva esse número juntamente com o 
#ódigo do curso correspondente (supor que não haja empate);  
#c.	calcule e escreva o total de candidatos;

total_candidatos = 0
quantidade_feminino = 0
curso_maior = 0
curso = 0

while True:
    numero_candidatos = 0
    porcentagem_feminino = 0
    numero_candidatos = 0
    maior_numero_candidatos = 0

    codigo_curso = int(input("Digite o código do curso ou (0) para encerrar: "))
    

    if codigo_curso == 0:
        print("Encerrando...\n")
        break
    numero_vagas = int(input("Número de vagas: "))

    numero_masculino = int(input("Número de candidatos do sexo masculino: "))
    if numero_masculino > 0:
        numero_candidatos += numero_masculino

    numero_feminino = int(input("Número de candidatos do sexo feminino: "))

    if numero_feminino > 0:
        numero_candidatos += numero_feminino

    if numero_candidatos > maior_numero_candidatos:
        curso_maior = codigo_curso
        maior_numero_candidatos += numero_candidatos

    total_candidatos += numero_candidatos
    candidatos_maior = maior_numero_candidatos

    #a.calcule e escreva, para cada curso, o número de candidatos por vaga e a porcentagem de 
    #candidatos do sexo feminino (escreva também o código correspondente do curso);
    if numero_candidatos > 0: 
        porcentagem_feminino = (numero_feminino * 100) / (numero_candidatos)
        print(f"Para o curso: {codigo_curso}\nNúmero de candidatos: {numero_candidatos}")
        print(f"Porcentagem de candidatos sexo do femiminino: {porcentagem_feminino:.2f}")
    else:
        print("Erro: Informações não fornecidas!")
        continue

    curso += 1


if  curso > 1:
    print("VISÃO GERAL")
    #b.	determine o maior número de candidatos por vaga e escreva esse número juntamente com o 
    #ódigo do curso correspondente (supor que não haja empate);
    if candidatos_maior > 0:
        print(f"Maior número de candidatos por vaga: {candidatos_maior} (curso: {curso_maior})")
        
    else:
        print("Não existe dados para maior números de vagas.")

    #c.	calcule e escreva o total de candidatos;
    print(f"Total candidadatos: {total_candidatos}")
elif curso == 0:
    print()
else:
    print("Não existe curso com maior vaga porque apenas 1 curso foi fornecido.")