#Escreva uma estrutura modular com um procedimento que recebe um parâmetro inteiro
#  ‘n’ e que ao ser chamado imprime uma sequência de linhas como mostram as figuras
#  a seguir, para n = 4:
#*=========*
#*       1 *
#*     2 2 *
#*   3 3 3 *
#* 4 4 4 4 *
#*=========*
#* 4 4 4 4 *
#*   3 3 3 *
#*     2 2 *
#*       1 *
#*=========*

def sequencia(n):
   
    # 1 ate 4

    for i in range(1, n + 1):
        print('*', end=' ')
        for k in range(n - i):
            print(' ', end=' ')
        for j in range(i):
            print(i, end=' ')
        print('*')    
        

    # 4 ate 1
    
    for i in range(n, 0, -1):
        print('*', end=' ')
        for k in range(n - i):
            print(' ', end=' ')
        for j in range(i):
            print(i, end=' ')
        print('*')
    
# Exemplo:
sequencia(4)