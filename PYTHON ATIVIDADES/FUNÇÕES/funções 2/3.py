# Desenvolva uma estrutura modular com uma função que recebe através de 
# parâmetro a cadeia de caracteres e retorna:
#-1, se existir na cadeia pelo menos um caractere que não seja um 
# caractere numérico e alfabético.
#0, se a quantidade de caracteres numéricos da cadeia for maior ou 
# igual a quantidade de caracteres alfabéticos.
#1, se a quantidade de caracteres alfabéticos da cadeia for maior 
# que quantidade de caracteres numéricos.

def verificar(cadeia):
##-1, se existir na cadeia pelo menos um caractere que não seja um 
# caractere numérico e alfabético.
  for i in cadeia:
    
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    if i.upper() not in alfabeto and i != int:
      return -1
    

string = "..."

print(verificar(string))