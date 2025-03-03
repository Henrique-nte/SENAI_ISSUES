#Por exemplo, se no dia 0 da epidemia 3 pessoas são infectadas e o fator reprodutivo R é igual a
#2, então no dia 1 outras 6 pessoas são infectadas (3 + 6 = 9 pessoas no total), no dia 2 outras 12
#pessoas são infectadas (3 + 6 + 12 = 21 pessoas no total), no dia 3 outras 24 pessoas infectadas
#(3 + 6 + 12 + 24 = 45 pessoas no total), e assim por diante.
#Dados o número inicial de pessoas infectadas no dia 0 e o fator reprodutivo R da epidemia, escreva
#um programa para determinar qual o número de dias necessários para a epidemia infectar P ou
#mais pessoas no total.
infectados = 0
contador = 0
resultado = 0
dias = 0
soma = 0
i = 0

n = int(input("Número de pessoas infectadas no dia 0: "))
r = int(input("O fator reprodutivo R da infecção: "))
p = int(input("O número alvo de pessoas infectadas: "))

while dias < p:
    dias += n * r


print(soma)
print(dias)