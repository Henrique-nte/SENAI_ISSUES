#11 - Verificar se um número é positivo ou negativo
#Peça ao usuário para inserir um número e imprima se o número é "Positivo" 
#ou "Negativo".

numero = int(input("Digite um número: "))
if numero > 0:
    print("Positivo.")
if numero < 0:
    print("Negativo.")
if numero == 0:
    print("Zero")