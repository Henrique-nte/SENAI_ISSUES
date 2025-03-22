#Peça ao usuário para inserir uma frase. Depois, substitua todas as vogais da frase por
# * e exiba o resultado.

#📌 Desafio Extra: Permita que o usuário escolha com qual caractere substituir as vogais.

frase = input("Digite uma frase: ")
palavra = ''
vogais = ['a','e','i','o','u']

caractere = input("Qual caractere irá substituir as vogais: ")

for i in frase:

    if i in vogais and i != " ":
        i = caractere
    palavra += i
   
print(palavra)
