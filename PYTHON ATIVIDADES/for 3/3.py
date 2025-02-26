#Escreva um programa que conte quantos dígitos um número possui. Por exemplo, 
#se o número fornecido for 12345, a resposta deve ser 5. Utilize o loop for 
#para percorrer os dígitos.
n = input("Digite um número: ")
contador = 0

for digito in (n):
    contador += 1

print(contador)


    
