#20 - Escolher dia da semana
#Solicite ao usuário um número de 1 a 7 e imprima o nome 
#do dia correspondente. Exemplo: 1 = "Domingo", 2 = 
#"Segunda-feira", etc.

n = int(input("Digite um número: "))

match n:
    case 1:
        print("Domingo.")
    case 2:
        print("Segunda.")
    case 3:
        print("Terça.")
    case 4:
        print("Quarta.")
    case 5:
        print("Quinta.")
    case 6:
        print("Sexta.")
    case 7:
        print("Sábado.")
    case _:
        print("Número inválido.")
