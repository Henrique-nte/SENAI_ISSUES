#18 - Calcular a média de três notas
#Peça para o usuário inserir três notas e calcule a média. 
#Exiba "Aprovado" se a média for maior ou igual a 7 e "Reprovado" 
#caso contrário.

nota1 = int(input("Digite a 1° nota: "))
nota2 = int(input("Digite a 2° nota: "))
nota3 = int(input("Digite a 3° nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
