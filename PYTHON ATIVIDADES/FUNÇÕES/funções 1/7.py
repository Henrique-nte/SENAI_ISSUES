#Desenvolver uma estrutura modular com uma função que recebe através
#de parâmetro um número inteiro e retorna
#o fatorial deste número.

def calculo(num):
    i = num
    fatorial = num

    while i > 1:
        i -= 1
        fatorial *= i
    print(fatorial)

numero = 7
calculo(numero)