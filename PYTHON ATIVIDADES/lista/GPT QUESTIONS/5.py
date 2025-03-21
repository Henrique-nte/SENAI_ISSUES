#Peça ao usuário para inserir uma frase. Depois, substitua todas as vogais da frase por
# * e exiba o resultado.

#📌 Desafio Extra: Permita que o usuário escolha com qual caractere substituir as vogais.

frase = input("Digite uma frase: ")
vogais = ['a','e','i','o','u']
verificador = 0
contador = 0
lista = []

caractere = input("Qual caractere irá substituir as vogais: ")

for i in frase:
    if i in vogais:
        i = caractere 
    lista.append(i)
    
string = ''
print(lista)
lista = string
print(string)