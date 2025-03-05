#2.	A companhia ABC-LOC deseja contrair um empréstimo no Banco Mercantil de Fomento. Para tanto deseja calcular 
#quantos anos seriam necessários para o pagamento do empréstimo sabendo que o banco cobra 3,5% de juros ao mês. 
#A companhia deseja fazer pagamentos mensais fixos no valor de 10% da dívida inicial mensalmente. Fazer um algoritmo
#que calcule quantos meses serão necessários para o pagamento total da dívida.

emprestimo = int(input("Valor do empréstimo: "))
pagamento = (emprestimo / 100) * 10
total = 0
mes = 0

juros  = 0.035 * emprestimo

while total < emprestimo:
        emprestimo += juros
        total += pagamento
        mes += 1
        

print(f"Mês: {mes}")
