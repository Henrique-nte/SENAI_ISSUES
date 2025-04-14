#Desenvolver uma estrutura modular com um procedimento que recebe através de parametro
#um número inteiro e apresenta a tabuada deste número

def mensagem(num):
    for i in range(10):
        i += 1
        total = num * i
        print(num, "*", i, "=", total)

number = int(input("Quer saber a tabuada de qual número: "))
mensagem(number)