#23 - Classificar notas
#Peça para o usuário inserir uma nota e, de acordo com a nota, classifique como:
#a.	0 a 4: "Reprovado"
#b.	5 a 6: "Recuperação"
#c.	7 a 10: "Aprovado"

nota = int(input("Digite uma nota: "))

match nota:
    case 0 | 1 | 2 | 3 | 4:
        print("Reprovado.")
    case 5 | 6:
        print("Recuperação.")
    case 7 | 8 | 9 | 10:
        print("Aprovado")
    case _:
        print("Nota inválida.")