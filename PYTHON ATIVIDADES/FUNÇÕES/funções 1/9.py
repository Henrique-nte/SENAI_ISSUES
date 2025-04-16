#Desenvolver uma estrutura modular com uma função que calcula e retorna o Gasto Energético Basal (GEB), utilizando
#as seguintes fórmulas:
#● Para os homens: GEB = 66.47 + (13.75 * PC) + (5 * Alt) – (6.76 * I);
#● Para as mulheres: GEB = 655.1 + (9.56 * PC) + (1.85 * Alt) – (4.67 * I);
#Onde: PC- Peso Corporal em “kg”; Alt- altura em “cm” e I- Idade. Obs. No corpo do programa principal deve-se obter
#os dados de entrada: sexo, peso corporal, altura e idade e a função deverá receber estes dados através de parâmetros
#retornando o gasto energético basal calculado.

def calculo(sexo, pc, alt, i):
    #● Para os homens: GEB = 66.47 + (13.75 * PC) + (5 * Alt) – (6.76 * I);
    
    geb = 0
    if sexo == "M":
        geb = 66.47 + (13.75 * pc) + (5 * alt) - (6.76 * i)
    elif sexo == "F":
        geb = 655.1 + (9.56 * pc) + (1.85 * alt) - (4.67 * i)
    return geb

sexo = "f".upper()
peso = 70
altura = 170
idade = 18

print(calculo(sexo, peso, altura, idade))