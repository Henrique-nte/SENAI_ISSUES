#16.Comparação entre três números
#Peça para o usuário inserir três números e 
#mprima o maior e o menor entre eles.

nu1 = float(input("Digite o 1 primeiro: "))
nu2 = float(input("Digite o 2 primeiro: "))
nu3 = float(input("Digite o 3 primeiro: "))

maior = nu1
menor = nu1

if nu2 > maior:
    maior = nu2
elif nu3 > maior:
    maior = nu3

if nu2 < menor:
    menor = nu2
elif nu3 < menor:
    menor = nu3

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
    