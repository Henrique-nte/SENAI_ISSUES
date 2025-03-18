#1- Uma empresa utiliza os códigos 1 para funcionários do setor administrativo e 2 para
# os funcionários do setor operacional. Faça um programa que receba o código e o salário
# de 20 funcionários. Calcule e mostre:

#●	A média salarial do setor administrativo.
#●	A média salarial do setor operacional.
#●	O total de salários pagos pela empresa.
#●	A quantidade de funcionários em cada setor.

pessoas_adminitrativo = 0
pessoas_operacional = 0
soma_salario_operacional = 0
soma_salario_administrativo = 0
soma_salarios = 0

for i in range(20):
    print("Digite 1 para setor ADMINISTRATIVO\nDigite 2 para setor OPERACIONAL")
    codigo = int(input("Escolha uma opção: "))
    salario = int(input("Digite o salário: "))
    soma_salarios += salario

    match codigo:
        case 1:
            soma_salario_administrativo += salario
            pessoas_adminitrativo += 1
        case 2:
            pessoas_operacional += 1
            soma_salario_operacional += salario


if pessoas_adminitrativo > 0:
    media_salario_administrativo = soma_salario_administrativo / pessoas_adminitrativo 
else:
    media_salario_administrativo = soma_salario_administrativo / 1 

if pessoas_operacional > 0:
    media_salario_operacional = soma_salario_operacional / pessoas_operacional 
else:
    media_salario_operacional = soma_salario_operacional / 1

print("\nVISÃO GERAL\n")

#●	A média salarial do setor administrativo.
print(f"Media administrativo: {media_salario_administrativo}")

#●	A média salarial do setor operacional.
print(f"Media operacional: {media_salario_operacional}")

#●	O total de salários pagos pela empresa.
print(f"Total de salários pagos: {soma_salarios}")

#●	A quantidade de funcionários em cada setor.
print(f"Setor administrativo quantidade de pessoas: {pessoas_adminitrativo}")
print(f"Setor operacional quantidade de pessoas: {pessoas_operacional}")

