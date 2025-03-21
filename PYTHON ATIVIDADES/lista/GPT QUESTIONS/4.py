#Peça ao usuário para inserir uma palavra ou frase e armazene os caracteres em uma lista.
# Depois, verifique se a palavra ou frase é um palíndromo (ou seja, se pode ser lida da 
#mesma forma de trás para frente).

#📌 Desafio Extra: Ignore espaços e acentos ao verificar o palíndromo.
array = []
lista = []
contador = 0
print("Verificador de palíndromos.")

while True:
    palavra = input("Digite um palavra: ")

    for i in palavra:
        array.append(i)

    for i in range(len(array)):
        if array[i] == None:
            del array[i]
    print(array)
    i = len(array)
    while i > 0:
        i -= 1
        lista.append(array[i])
    
    for i in range(len(array)):
        if array[i] == lista[i]:
            contador += 1
    if contador == len(array):
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")



