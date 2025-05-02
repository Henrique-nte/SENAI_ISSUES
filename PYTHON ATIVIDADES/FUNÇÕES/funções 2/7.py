#8  - Escreva uma função que, 
#recebendo como parâmetro um número inteiro, retorne este número
#escrito ao contrário.
def verificar_palindromo(numero):
    contrario = []
    contador = 0
    
    for i in range(len(numero) -1, -1, -1):
        contrario.append(numero[i])

    j = 0
    for i in numero:
        if i == contrario[j]:
            contador += 1
            j += 1 

    string = ''

    if contador == len(numero):
        for i in numero:
            string += i 
        print(string,'|',end = '')
        
#A seguir, implementar uma estrutura modular
#que determine e escreva, usando a função implementada, todos os 
#números palíndromos entre 1000 e 10000.

def de1000a10000():
    for i in range(1000, 10000):
        verificar_palindromo(str(i))   

print(de1000a10000())
    
