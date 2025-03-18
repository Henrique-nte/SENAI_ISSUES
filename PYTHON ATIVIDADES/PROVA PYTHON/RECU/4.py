#4- Uma sequência de 50 números será informada pelo usuário. Escreva um programa que:
#●	Conte quantos desses números são múltiplos de 3.
#●	Exiba a soma de todos os números pare

quantidade_3 = 0
soma_par = 0

for i in range(50):
    numero = float(input(f"Digite o número {i + 1}: "))
    #●	Conte quantos desses números são múltiplos de 3.
    if numero % 3 == 0:
        quantidade_3 += 1

    if numero % 2 == 0:
        soma_par += numero

print(f"Quantidade de números múltiplos de 3: {quantidade_3}")

#●	Exiba a soma de todos os números pares
print(f"Soma de todos os números pares: {soma_par}")