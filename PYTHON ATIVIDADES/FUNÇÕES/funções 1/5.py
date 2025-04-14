#Desenvolver uma estrutura modular com uma função que recebe através de parâmetro
#um número inteiro e retorna
#um valor booleano indicando se o número corresponde a um ano bissexto. 
#Um ano é bissexto quando for divisível
#por 4 e não for divisível por 100. Também são bissextos os divisíveis por 400.

def calculo(numero):
    if (numero % 4 == 0 and numero % 100 != 0) or (numero % 400 == 0):
        return True
    else:
        return False

ano = 2000

print(calculo(ano))