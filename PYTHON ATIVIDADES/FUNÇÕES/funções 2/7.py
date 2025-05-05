#7 - Escreva uma função que, 
#recebendo como parâmetro um número inteiro, retorne este número
#escrito ao contrário.
def verificar_palindromo(numero):
    contrario = []
    string = ''
    contador = 0
    j = 0
    
    for i in range(len(numero) -1, -1, -1):
      contrario.append(numero[i])
      if contrario[j] == numero[j]:
         contador += 1
         j += 1

    if contador == len(numero):
      for i in numero:
          string += i
      print(string)
       
#A seguir, implementar uma estrutura modular
#que determine e escreva, usando a função implementada, todos os 
#números palíndromos entre 1000 e 10000.

for i in range(1000, 10000):
    verificar_palindromo(str(i))