#Escreva uma estrutura modular com um procedimento que recebe um parâmetro inteiro ‘n’
#  e que ao ser chamado imprime uma sequência de linhas como mostram as figuras a seguir, para n = 9:
#                1 * 1
#              2 2 * 2 2
#            3 3 3 * 3 3 3
#          4 4 4 4 * 4 4 4 4
#        5 5 5 5 5 * 5 5 5 5 5
#      6 6 6 6 6 6 * 6 6 6 6 6 6
#    7 7 7 7 7 7 7 * 7 7 7 7 7 7 7
#  8 8 8 8 8 8 8 8 * 8 8 8 8 8 8 8 8
#9 9 9 9 9 9 9 9 9 * 9 9 9 9 9 9 9 9 9
#*************************************
#9 9 9 9 9 9 9 9 9 * 9 9 9 9 9 9 9 9 9
#  8 8 8 8 8 8 8 8 * 8 8 8 8 8 8 8 8
#    7 7 7 7 7 7 7 * 7 7 7 7 7 7 7
#      6 6 6 6 6 6 * 6 6 6 6 6 6
#        5 5 5 5 5 * 5 5 5 5 5
#          4 4 4 4 * 4 4 4 4
#            3 3 3 * 3 3 3
#              2 2 * 2 2
#                1 * 1

def sequencia(n):
  for i in range(1, n + 1):
    print("*", end = " ")
    for j in range(n - i):
      print(' ', end=' ')
    for k in range(i):
      print(i, end=' ')
    print('*')

  for i in range(n, 0, - 1):
    print("*", end = " ")
    for j in range(n - i):
      print(' ', end=' ')
    for k in range(i):
      print(i, end=' ')
    print('*')

sequencia(9)