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
            for i in range(1):

                valor = input(f"Digite o nome do contato {i + 1}: ")
                nomes.append(valor)

                valor = int(input(f"Digite o telefone do contato {i + 1}: "))
                telefone.append(valor)

                valor = input(f"Digite o email do contato {i + 1}: ")
                email.append(valor)
        case 2:
            #EDITAR
            print("Editar contatos\n")
            response = input("Qual o nome do contato que você deseja editar: ")

            for i in range(1):
                if nomes[i] == response:
                    posicao = i
                    contador = 1

            if contador < 1:
                print("Nome não está nos seus contatos")
                continue

            print("1 - Editar Nome\n2 - Editar telefone\n3 - Editar Email\n4 - Voltar\n")
            resposta = int(input("Quais parâmetros do contato você deseja editar?"))

            match resposta:
                case 1:
                    valor = input("Nome novo: ")
                    nomes[posicao] = valor

                case 2:
                    valor = int(input("Telefone Novo: "))
                    telefone[posicao] = valor
                case 3:
                    valor = input("Email Novo: ")
                    email[posicao] = valor
                case _:
                    continue
        case 3:
            #EXCLUIR
            print("Excluir contatos\n")
            response = input("Qual o nome do contato que você deseja excluir: ")

            for i in range(1):
                if nomes[i] == response:
                    posicao = i
                    contador = 1

            if contador < 1:
                print("Nome não está nos seus contatos")
                continue

            print("1 - Excluir Nome\n2 - Excluir telefone\n3 - Excluir Email\n4 - Voltar\n")
            resposta = int(input("Quais parâmetros do contato você deseja editar?"))

            match resposta:
                case 1:
                    valor = input("Nome novo: ")
                    nomes[posicao] = valor

                case 2:
                    valor = int(input("Telefone Novo: "))
                    telefone[posicao] = valor
                case 3:
                    valor = input("Email Novo: ")
                    email[posicao] = valor
                case _:
                    continue


        case 4:

            #EXIBIR
            print("\nContatos")
            print("=" * 60)  # Linha de separação
            print(f"{'Nome':<20}{'Telefone':<20}{'Email':<20}")  # Cabeçalho
            print("-" * 60)  # Linha de separação

            for i in range(1):
                print(f"{nomes[i]:<20}{telefone[i]:<20}{email[i]:<20}\n")
    if resposta == 5:
        break
