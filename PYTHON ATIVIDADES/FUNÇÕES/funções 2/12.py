#12 - Desenvolva uma estrutura modular com a função para calcular
# e retornar o fatorial de um número.

def fatorial(numero):
    auxiliar = numero
    while auxiliar > 1:
        auxiliar -= 1
        numero *= auxiliar
    return numero

number = 6
print(fatorial(number))