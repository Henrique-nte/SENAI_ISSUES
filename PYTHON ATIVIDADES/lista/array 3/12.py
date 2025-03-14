#12- Considere um vetor de trajetórias de 9 elementos, onde cada elemento possui o 
#valor do próximo elemento do vetor a ser lido.                    

#Índice   0   1    2    3    4    5    6    7     8     9                      
#Valor        5    7    6    9     2   8    4     0     3
            
#Assim, a seqüência da leitura seria 1, 5, 2, 7, 4, 9, 3, 6, 8, 0            


indice =    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sequencia = [5, 7, 6, 9, 2, 8, 4, 0, 3]
leitura = []
num = 0

for i in range(len(indice)):
    #cada elemento possui o valor do próximo elemento do vetor a ser lido.
    atual = sequencia[num]
    leitura.append(atual)
    num = atual - 1

print(leitura)