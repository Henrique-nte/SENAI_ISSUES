#2 - Desenvolva uma função que recebe através de parâmetros, 
#duas cadeias de caracteres e retorna verdadeiro se as 
#cadeias são iguais e falso caso contrário. Obs. fazer 
#comparações “caractere por caractere” até definir o 
#valor de retorno.

def verificar(cadeia, chain):
  j = 0
  for i in cadeia:
    if i != chain[j]:
      return False
    j += 1
  return True

string = 'abc'
list = 'abc'

print(verificar(string, list))