#6.	Crie um programa que ajude a programar turnos de trabalho em uma empresa. 
#O usuário deve informar o dia da semana (1 a 7, sendo 1 para domingo e 7 para sábado). 
#O programa deve exibir a programação dos turnos:
#●	Dias úteis (segunda a sexta): Turno Normal
#●	Sábado: Turno Reduzido
#●	Domingo: Sem Trabalho

dia = int(input("Dia da semana: "))

match dia:
    case 1:
        print("Sem Trabalho.")
    case 2 | 3 | 4 | 5:
        print("Turno Normal.")
    case 6:
        print("Turno Normal.")
    case 7:
        print("Turno reduzido.")
    case _:
        print("Número inválido.")
        