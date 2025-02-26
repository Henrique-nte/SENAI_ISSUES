#12.	Maior de dois números
#Solicite dois números ao usuário e imprima o maior deles.

numero = float(input("Digite um primeiro número: "))
numero = float(input("Digite um segundo número: "))

maior = 0

while (maior < numero):
    if numero > maior:
        maior = numero

print(f"Número Maior: {maior}")