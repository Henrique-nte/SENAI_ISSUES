#Desenvolver uma estrutura modular com uma função que recebe através de 
#parâmetro um número inteiro que
#corresponde a um mês do ano e retorna com o nome desse mês. Por exemplo, 
#se o mês enviado for 1 a função
#deverá retorna janeiro, se o mês enviado for 2 a função deverá retornar
#fevereiro e assim por diante

def calculo(num):
    match num:
        case 1:
            print("Domingo")      
        case 2:
            print("Segunda")      
        case 3:
            print("Terça")      
        case 4:
            print("Quarta")      
        case 5:
            print("Quinta")      
        case 6:
            print("Sexta")      
        case 7:
            print("Sábado")
        case _:
            print("Número inválido")    

dia = 1
calculo(dia)