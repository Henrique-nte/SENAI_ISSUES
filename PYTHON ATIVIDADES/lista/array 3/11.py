#11- Você está desenvolvendo um aplicativo de agenda de contatos em JS. Crie um programa que permita ao 
# usuário adicionar, editar, excluir e visualizar contatos em sua agenda. Os contatos devem ser armazenados
# em vetores que incluem nome, número de telefone e email.

nomes = []
telefone = []
email = []

while True:

    print("1 - Adicionar\n2 - Editar\n3 - Excluir\n4 - Exibir\n5 - Sair")
    resposta = int(input("Digite a operação que você deseja realizar: "))

    match resposta:
        case 1: 

            print("Adicionando contatos")

            #ADICIONAR
            for i in range(2):

                valor = input(f"Digite o nome do contato {i + 1}: ")
                nomes.append(valor)

                valor = input(f"Digite o telefone do contato {i + 1}: ")
                telefone.append(valor)

                valor = input(f"Digite o email do contato {i + 1}: ")
                email.append(valor)
        case 2:
            #EDITAR
            print("Editar contatos\n")
            response = input("Qual o nome do contato que você deseja editar")

            if response in nomes:

                print("1 - editar Nome\n 2 - editar telefone\n 3 - Editar Email")
                resposta = input("Quais parâmetros do contato você deseja editar?")


            else:
                print("Nome não está na lista")
                continue

        case 4:

            #EXIBIR
            print("\nContatos")
            print("=" * 60)  # Linha de separação
            print(f"{'Nome':<20}{'Telefone':<20}{'Email':<20}")  # Cabeçalho
            print("-" * 60)  # Linha de separação

            for i in range(2):
                print(f"{nomes[i]:<20}{telefone[i]:<20}{email[i]:<20}")
    if resposta == 5:
        break
