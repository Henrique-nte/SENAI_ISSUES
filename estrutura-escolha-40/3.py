#Fazer um algoritmo para imprimir o conceito de um aluno, dada a sua nota.
#Supor notas inteiras somente. O critério para conceitos é o seguinte:
#nota inferior a 3 - conceito E
#nota de 3 a 5 - conceito D
#notas 6 e 7 - conceito C
#notas 8 e 9 - conceito B
#nota 10 - conceito A

nota = int(input("Digite sua nota: "))

if nota < 3:
    print("Conceito E")
elif nota >= 3 and nota <= 5:
    print("Conceito D")
if nota > 6:
    print("Conceito D")


