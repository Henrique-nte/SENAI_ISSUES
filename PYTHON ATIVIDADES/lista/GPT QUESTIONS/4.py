#Peça ao usuário para inserir uma palavra ou frase e armazene os caracteres em uma lista.
# Depois, verifique se a palavra ou frase é um palíndromo (ou seja, se pode ser lida da 
#mesma forma de trás para frente).
#📌 Desafio Extra: Ignore espaços e acentos ao verificar o palíndromo.
array = []
array_temporario = []
lista = []
espacos = []
contador = 0

print("Verificador de palíndromos.")

while True:
    palavra = input("Digite um palavra: ")

    #Percorre todos os caracteres
    for i in palavra:
        #Ignora espaços
        if i != " ":
            array.append(i)
    print(array)

    #Lógica para descobrir se é um palíndromo
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



