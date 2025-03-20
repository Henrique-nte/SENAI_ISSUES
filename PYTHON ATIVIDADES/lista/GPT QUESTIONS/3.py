#Crie um programa que solicite ao usuário uma frase e, utilizando um laço de repetição, 
#conte quantas vogais (a, e, i, o, u) existem na frase. Exiba o total de vogais encontradas.

frase = input("Digite uma frase: ")
verificador = 0

for contador in frase:
    if contador == 'a' or contador == 'e' or contador == 'i' or contador == 'o' or contador == 'u':
        verificador += 1

print(verificador)