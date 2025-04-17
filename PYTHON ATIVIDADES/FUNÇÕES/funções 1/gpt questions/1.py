#Crie uma função que receba duas palavras e retorne True se a 
#primeira for prefixo da segunda.
lista = []
def calculo(word, word_2):
    contador = 0

    for i in word_2:
        lista.append(i)
    for i in word:
        contador += 1

    if contador >= 2 and contador <= 4:
        return True
    else:
        return False
    
palavra = "pinto"
palavra_2 = "desritmia"

print(calculo(palavra, palavra_2))