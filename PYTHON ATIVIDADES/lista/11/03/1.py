#1 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em um vetor. 
#Calcule e mostre a maior e a menor temperatura do ano e em que mês elas ocorreram 
#(mostrar o mês por extenso: 1- Janeiro, 2 – Fevereiro). Desconsidere empates.

temperatura_media_cada_mes = []
mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
 "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];

maior_temperatura = float("-inf")
menor_temperatura = float("inf")

for i in range(3):
    
    valor = float(input(f"Digite a temperatura do mês {mes[i]}: "))
    temperatura_media_cada_mes.append(valor)

    if valor > maior_temperatura:
        maior_temperatura = valor
        
        mes_maior = mes[i]

    elif valor < menor_temperatura:
        menor_temperatura = valor
        mes_menor = mes[i]
        

print(f"O mês {mes_maior} teve a Maior temperatura {maior_temperatura}")
print(f"O mês {mes_menor} teve a Menor temperatura {menor_temperatura}")