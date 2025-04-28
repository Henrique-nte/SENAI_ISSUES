# 3 - Desenvolva uma estrutura modular com uma função que recebe através de 
# parâmetro a cadeia de caracteres e retorna:
#-1, se existir na cadeia pelo menos um caractere que não seja um 
# caractere numérico e alfabético.
#0, se a quantidade de caracteres numéricos da cadeia for maior ou 
# igual a quantidade de caracteres alfabéticos.
#1, se a quantidade de caracteres alfabéticos da cadeia for maior 
# que quantidade de caracteres numéricos.

def verificar(cadeia):
  numericos = 0
  caracteres = 0

  for i in cadeia:
    if ('A' <= i <= 'Z'):
      caracteres += 1
    elif ('0' <= i <= '9'):
      numericos += 1
    else:
     return -1
  if numericos > caracteres:
    return 0
  else:
    return 1
    
string = "11a".upper()
print(verificar(string))