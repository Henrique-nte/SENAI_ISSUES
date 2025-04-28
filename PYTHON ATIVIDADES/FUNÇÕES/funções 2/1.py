#1 - Desenvolva uma estrutura modular com uma função que recebe através de parâmetro uma
#cadeia de caracteres e retorna verdadeiro se “todos” os caracteres alfabéticos
#da cadeia são minúsculos e falso caso contrário.

def verificar(cadeia):
  for i in cadeia:
    if "A" <= i <= "Z":
      return False
  return True  
string = "abcd"
print(verificar(string))
