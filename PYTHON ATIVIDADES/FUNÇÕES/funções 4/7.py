#Escreva uma estrutura modular com um procedimento que recebe um parâmetro inteiro
#  ‘n’ e que ao ser chamado imprime uma sequência de linhas como mostram as figuras
#  a seguir, para n = 4:
#*=========*
#*       1 *
#*     2 2 *
#*   3 3 3 *
#* 4 4 4 4 *
#***********
#* 4 4 4 4 *
#* 3 3 3   *
#* 2 2     *
#* 1       *
#*=========*

matriz = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]
]

def sequencia(n):
    string_n = str(n)
    
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j > 2:
                print(matriz[i][j], end = '')

numero = 4
sequencia(numero)