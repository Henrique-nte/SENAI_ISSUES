#3- Uma pesquisa de satisfação foi realizada com 40 clientes de uma loja, pedindo que avaliassem 
#o atendimento como: péssimo = 1, regular = 2, bom = 3, excelente = 4. Faça um programa que leia a 
#avaliação e a idade dos clientes e exiba:

#●	A média de idade dos clientes que avaliaram como "excelente".
#●	O total de clientes que avaliaram como "péssimo".
#●	A porcentagem de clientes que avaliaram como "bom" em relação ao total.

soma_idade_4 = 0
total_pessimo = 0
total_bom = 0

for i in range(40):

    print("Para PÉSSIMO digite (1)")
    print("Para REGULAR digite (2)")
    print("Para BOM digite (3)")
    print("Para EXCELENTE digite (4)")
    escolha = int(input("Escolha uma opção: "))
    idade = int(input(f"Idade do cliente {i + 1}: "))


    match escolha:
        case 1:
            total_pessimo += 1
        case 3:
            total_bom += 1
        case 4:
            soma_idade_4 += idade

#●	A média de idade dos clientes que avaliaram como "excelente".
media_idade_excelente = soma_idade_4 / 40
print(f"Media de idade dos cliente que avaliaram como 'excelente': {media_idade_excelente}")

#●	O total de clientes que avaliaram como "péssimo".
print(f"Clientes que avaliaram como 'péssimo': {total_pessimo}")

#●	A porcentagem de clientes que avaliaram como "bom" em relação ao total.
porcentagem_bom = (total_bom * 100) / 40
print(f"porcentagem de clientes que avaliaram como 'bom' em relação ao total: {porcentagem_bom}")