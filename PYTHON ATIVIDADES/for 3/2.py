#Escreva um programa que mostre a tabuada de um número N fornecido pelo usuário de 
#forma invertida (começando do maior valor, por exemplo, 10 até 1)

#2-	Fazer um programa que calcule a tabuada de qualquer número, 
#e o limite de cálculo deve ser definido pelo usuário:

numero = int(input("Você quer saber a tabuada de qual número: "))
limite = int(input("Qual o limite?: "))

i = limite

while i > 0:
    total = numero * i
    print(f"{numero} x {i} = {total}")
    i -= 1

