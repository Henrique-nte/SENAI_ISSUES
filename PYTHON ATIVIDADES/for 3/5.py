#Faça uma Programa que receba, como entrada, uma lista de números positivos ou negativos
# finalizada com o número zero e forneça, como saída, a soma dos números positivos, a 
#soma dos números negativos e a soma das duas somas parciais e mostre os números pares
# e ímpares ao final.
while numero != 0:
    numero = int(input("Digite um número: "))
    positivos = 0
    negativos = 0  
    pares = 0
    impares = 0
    soma_total = 0             
    if numero > 0:
        positivos += numero
        soma_total += numero
    elif numero < 0:
        negativos += numero
        soma_total += numero
    if numero %2 == 0:
        pares += numero
        soma_total += numero
    elif numero %2 == 1:
        impares += numero
        soma_total += numero
    
print(positivos)
print(negativos)
print(pares)
print(impares)
print(soma_total)