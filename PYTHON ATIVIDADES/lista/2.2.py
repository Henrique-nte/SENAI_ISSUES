#2 - Utilizando vetores, crie um programa que organize uma quantidade
# qualquer de números inteiros fornecidos pelo usuário da seguinte forma
# primeiros os números pares em prde, crescemte e depois os números impares 
#em ordem de-crescente

n = int(input("Quantos números você deseja digitar: "))

numeros = []
pares = []
impares = []
pares = []

for i in range(n):
   numbers = int(input(f"Digite o número {i + 1}: "))
   numeros.append(numbers)
   
   if numeros[i] % 2 == 0:
      pares.append(numeros[i])

   elif numeros[i] % 2 != 0:
        impares.append(numeros[i])

pares.sort()
print(pares)

impares.sort(reverse = True)
print(impares)

