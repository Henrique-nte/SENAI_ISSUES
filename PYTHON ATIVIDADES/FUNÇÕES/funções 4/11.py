#Escreva uma estrutura modular com um procedimento que recebe um parâmetro inteiro 
# ‘n’ e que ao ser chamado imprime uma sequência de linhas como mostram 
# as figuras a seguir, para n = 7:
#      1
#    3 3 3
#  5 5 5 5 5
#7 7 7 7 7 7 7
#=============

def sequencia(n):
    for i in range(1, n):
        for j in range(n - i):
            print(i, end=' ')

sequencia(7)