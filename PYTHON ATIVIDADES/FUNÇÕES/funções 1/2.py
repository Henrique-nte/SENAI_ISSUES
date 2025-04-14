#Desenvolver uma estrutura modular com uma função que recebe através de parâmetro um 
#número inteiro e retorna
#o valor absoluto (positivo) deste número.

def absoluto(num):
    if num < 0:
        num *= - 1
    return num
    
numero = -25
print(absoluto(numero))