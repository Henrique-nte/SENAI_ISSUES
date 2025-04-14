#Desenvolver uma estrutura modular com uma função que recebe através
# de parâmetro dois números inteiros e
#retorna um valor booleano indicando se o primeiro número é múltiplo do segundo.

def calculo(num, num2):
    if num % num2 == 0:
        return True
    else:
        return False
    
numero = 5
numero2 = 5

print(calculo(numero, numero2))