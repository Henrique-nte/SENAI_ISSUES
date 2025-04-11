#Peça ao usuário para inserir uma frase. Depois, substitua todas as vogais da frase por
# * e exiba o resultado.

#📌 Desafio Extra: Permita que o usuário escolha com qual caractere substituir as vogais.

frase = input("Digite uma frase: ").lower()
palavra = '' 
vogais = ['aeiou']

caractere = input("Qual caractere irá substituir as vogais: ").lower()

for i in frase:

    if i in vogais:
        i = caractere
    palavra += i
   
print(palavra)