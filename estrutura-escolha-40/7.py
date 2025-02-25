#7.	Desenvolva um programa que analise o desempenho de vendas de uma loja.
# O usuário deve informar o total de vendas em um mês. Com base no valor, 
#o programa deve classificar o desempenho de vendas:
#●	Abaixo de R$ 5.000: Desempenho Fraco
#●	Entre R$ 5.000 e R$ 10.000: Desempenho Regular
#●	Acima de R$ 10.000: Desempenho Excelente

vendas = float(input("Total de vendas: "))

if  vendas > 10000:
        print("Desempenho Excelente!")
elif  vendas >= 5000 and vendas <= 10000:
        print("Desempenho Regular!") 
elif  vendas < 5000:
        print("Desempenho Fraco!")
