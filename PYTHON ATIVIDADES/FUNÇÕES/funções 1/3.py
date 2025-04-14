#Desenvolver uma estrutura modular com uma função que recebe através
# de parâmetro um número inteiro e retorna
#um valor booleano indicando se o número é par ou não.

def verificador(num):
    if num % 2 != 0:
        return False
    else:
        return True

numero = 2
print(verificador(numero))