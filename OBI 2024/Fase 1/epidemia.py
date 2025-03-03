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

