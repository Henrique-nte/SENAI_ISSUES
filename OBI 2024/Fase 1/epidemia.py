#Por exemplo, se no dia 0 da epidemia 3 pessoas são infectadas e o fator reprodutivo R é igual a
#2, então no dia 1 outras 6 pessoas são infectadas (3 + 6 = 9 pessoas no total), no dia 2 outras 12
#pessoas são infectadas (3 + 6 + 12 = 21 pessoas no total), no dia 3 outras 24 pessoas infectadas
#(3 + 6 + 12 + 24 = 45 pessoas no total), e assim por diante.
#Dados o número inicial de pessoas infectadas no dia 0 e o fator reprodutivo R da epidemia, escreva
#um programa para determinar qual o número de dias necessários para a epidemia infectar P ou
#mais pessoas no total


#Por exemplo, se no dia 0 da epidemia 1 pessoa é infectada e o fator reprodutivo R é igual a 5, então
#  no dia 1 outras 5 pessoas são infectadas (1 + 5 = 6 pessoas no total), no dia 2 outras 25 pessoas
#  são infectadas (1 + 5 + 25 = 31 pessoas no total), no dia 3 outras 125 pessoas são infectadas 
# #(1 + 5 + 25 + 125 = 156 pessoas no total), e assim por diante.  

n = int(input("Número de pessoas infectadas no dia 0: "))
r = int(input("O fator reprodutivo R da infecção: "))
p = int(input("O número alvo de pessoas infectadas: "))

dia = 0
infectados_total = n  
novos_infectados = n  

while infectados_total < p:
    novos_infectados *= r  
    infectados_total += novos_infectados  
    dia += 1 

print(dia)
