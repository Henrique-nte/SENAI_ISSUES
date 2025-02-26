#2-	Fazer um programa que calcule a tabuada de qualquer número, 
#e o limite de cálculo deve ser definido pelo usuário:

numero = int(input("Você quer saber a tabuada de qual número: "))
limite = int(input("Qual o limite?: "))
i = 0
total = 0

#COM FOR
#for i in range(limite):
    #i += 1
    #total = numero * i
    #print(numero, "*", i, "=", total)

#COM WHILE
while (limite > i):
    i += 1
    total = numero * i
    print(numero, "*", i, "=", total)

