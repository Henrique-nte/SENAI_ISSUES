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

    for i in range(1, n):
        print('*', end=' ')
        for k in range(n - i):
            print(' ', end=' ')
        for j in range(i):
            print(i, end=' ')
        print('*')    
        
    print('*', end=' ')
    for i in range(n):
        print(n, end=' ')
    print('*')

     # 4 ate 1
    print('*', end=' ')
    for i in range(n):
        print(n, end=' ')
    print('*')

    for i in range(n - 1, 0, -1):
        print('*', end=' ')
        for k in range(n - i):
            print(' ', end=' ')
        for j in range(i):
            print(i, end=' ')
        print('*')
    
    

# Exemplo:
sequencia(4)