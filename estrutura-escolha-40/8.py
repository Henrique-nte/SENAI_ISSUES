#8.	Faça um programa que permita o cadastro de produtos em uma empresa.
##O programa deve exibir uma mensagem de confirmação com o tipo de produto cadastrado 
#e se ele é perecível ou não, de acordo com as seguintes regras:
#●	Alimento: Perecível
#●	Bebida: Não Perecível
#●	Vestuário: Não Perecível

nome = input("Nome do produto: ")
tipo = input("Tipo do produto: ").lower()
match tipo:
    case 'alimento':
        print("Este produto é Perecível")
    case 'bebida'| 'vestuario':
        print("Este produto não é Perecível")
    case _:
        print("Tipo de produto inválido.")

print(f"Produto {nome}, do tipo {tipo} cadastrado com sucesso!")



