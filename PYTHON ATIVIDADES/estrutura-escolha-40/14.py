#14	
#Peça para o usuário inserir a idade e classifique como "Criança", 
#"Adolescente", "Adulto" ou "Idoso", de acordo com os seguintes critérios:
#a.	0 a 12 anos: Criança
#b.	13 a 17 anos: Adolescente
#c.	18 a 60 anos: Adulto
#d.	Acima de 60 anos: Idoso

idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Criança.")
elif idade >= 13 and idade <= 17:
    print("Adolescente.")
elif idade >= 18 and idade <= 60:
    print("Adulto.")
elif idade > 60:
    print("Idoso.")
else:
    print("Idade inválida.")

