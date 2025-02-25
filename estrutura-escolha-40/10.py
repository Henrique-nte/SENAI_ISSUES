#Desenvolva um programa que avalie o desempenho de um funcionário com base em sua pontuação.
#O usuário deve informar a pontuação do funcionário. O programa deve classificar o desempenho 
#da seguinte maneira:
#●	0 a 5: Insatisfatório
#●	6 a 8: Satisfatório
#●	9 a 10: Excelente


pontuacao = float(input("Digite sua pontuação: "))

match pontuacao:
    case 0 | 1 | 2 | 3 | 4 | 5:
        print("Insatisfatório")
    case 6 | 7 | 8 :
        print("Satisfatório")
    case 9 | 10:
       print("Excelente!")
    case _:
        print("Pontuação não se encaixa em nenhuma categoria!")
