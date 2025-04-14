#2-Faça um programa que armazene as horas trabalhadas de 5 funcionários em uma semana. 
#Depois, calcule o total de horas trabalhadas e mostre o valor a ser pago a cada um, 
#sabendo que a hora de trabalho custa R$ 20.

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]


for i in range(5):
    horas = int(input(f"Horas de {dias[i]}:")) 