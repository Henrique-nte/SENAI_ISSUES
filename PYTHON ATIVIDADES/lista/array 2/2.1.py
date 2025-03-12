#1 faça um algotimo que leia a nota de 10 alunos de uma turma 
#e guatde-as em im vetor no final, mostre:

#a . Qual a média da turma;
#b . Quantos alunos estão acima da média da turma
#c . Qual foi a maior nota digitada
#d . Em que posição a maior nota aparece

notas = []
soma = 0
media = 0
alunos_acima_media = 0
maior_nota_digitada = (float("-inf"))
valores = []


for i in range(10):
    
    valor = int(input("Digite as notas: "))
    valores.append(valor)

    #c . Qual foi a maior nota digitada
    if valor > maior_nota_digitada:
          maior_nota_digitada = valor
          #d . Em que posição a maior nota aparece
          posicao = i

    soma += valor
    notas.append(valor)

    #a . Qual a média da turma;
    media  = soma / 10


for i in range(len(valores)):
    #b . Quantos alunos estão acima da média da turma   
    if valores[i] > media:
        alunos_acima_media += 1

    

print(f"Media da turma: {media}")
print(f"Alunos acima da media: {alunos_acima_media}")
print(f"Maior nota digitada: {maior_nota_digitada}")
print(f"Na posicão: {posicao + 1}")