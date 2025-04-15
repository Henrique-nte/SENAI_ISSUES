#Baseie-se na série de Fibonacci formada pela sequência: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, etc.
#Desenvolver uma estrutura
#modular com uma função que recebe através de parâmetro um número indicando a posição do termo
# e retorna o
#valor correspondente na sequência de Fibonacci

def calculo(posicao):
    Fn = 0
    i = 0
    for i in range(posicao):
        Fn = (Fn - 1) + (Fn - 2)

    return Fn

posicao = 5
print(calculo(posicao))