#Crie uma função que receba um valor em graus Ce F=(C×9/5)+32

def converter(c):
    f = ((c * 9) / 5) + 32
    return f

valor = 15
print(converter(valor))