#2.A companhia ABC-LOC deseja contrair um empréstimo no Banco Mercantil de Fomento. Para tanto deseja calcular 
#quantos anos seriam necessários para o pagamento do empréstimo sabendo que o banco cobra 3,5% de juros ao mês. 
#A companhia deseja fazer pagamentos mensais fixos no valor de 10% da dívida inicial mensalmente. Fazer um algoritmo
#que calcule quantos meses serão necessários para o pagamento total da dívida.
emprestimo = float(input("Valor do empréstimo: "))


pagamento = emprestimo * 1.035
# 10% da dívida inicial
pagamento = (emprestimo / 100) * 10

mes = 0

#Calcule quantos meses serão necessários para o pagamento total da dívida.
while emprestimo > 0:

    if pagamento > emprestimo:
        pagamento = emprestimo

    emprestimo -= pagamento
    
    mes += 1

print(f"Mês: {mes}")
