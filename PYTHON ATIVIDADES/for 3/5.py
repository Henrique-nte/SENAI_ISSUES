#Faça uma Programa que receba, como entrada, uma lista de números positivos ou negativos
#finalizada com o número zero e forneça, como saída, a soma dos números positivos, a 
#soma dos números negativos e a soma das duas somas parciais e mostre os números pares
#e ímpares ao final.
positivos = 0
negativos = 0  
pares = 0
impares = 0
soma_total = 0
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    if numero < 0:
        negativos += numero 
    else:
        positivos += numero 
    if numero %2 == 0:
        pares += numero
    elif numero %2 != 0:
        impares += numero
    soma_total += numero
    
print(f"Números Positivos: {positivos}")
print(f"Números Negativos: {negativos}")
print(f"Números Pares: {pares}")
print(f"Números Impares: {impares}")
print(f"Soma total: {soma_total}")