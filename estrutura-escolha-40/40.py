#Peça ao usuário para inserir um número inteiro. O programa deve verificar 
#se o número é par ou ímpar e positivo ou negativo, e então exibir uma mensagem 
#com essas classificações. Se o número for igual a zero, o programa deve indicar
#que é zero, que não é nem positivo nem negativo, nem par nem ímpar.

while True:
    n = int(input("Digite um número inteiro: "))

    if n == 0:
        print("Zero.")
        print("Não é par.")
        print("Não é impar.")
        print("Não é positivo.")
        print("Não é negativo.")
    elif n > 0:
        print("Positivo")
        if n % 2 == 0:
            print("Par.")
        elif n % 2 == 1:
            print("impar")
    elif n < 0:
        print("Negativo.")
        if n % 2 == 0:
            print("Par.")
        elif n % 2 == 1:
            print("impar")

