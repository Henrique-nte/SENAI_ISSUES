#Faça uma função que informe a quantidade de dígitos de um 
# determinado número inteiro informado.

def quantidade(inteiro):

    digitos = 0
    for i in inteiro:
        digitos += 1

    return digitos

number = 12345

print(quantidade(str(number)))