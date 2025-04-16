#Desenvolver uma estrutura modular com uma função que calcula e retorna o peso ideal, 
#utilizando as seguintes
#fórmulas:
#● Para homens: (72.7 * Alt) - 58;
#● Para mulheres: (62.1 * Alt) - 44.7.
#Obs. No corpo do programa principal deve-se obter os dados de entrada: sexo e altura (em metros)

def peso_ideal(sexo, alt):
    if sexo == "m":
        ps = (72.7 * alt) - 58
    if sexo == "f":
        ps = (62.1 * alt) - 44.7
    
    return ps

sexo = "f".lower()
altura = 1.70

print(peso_ideal(sexo, altura))