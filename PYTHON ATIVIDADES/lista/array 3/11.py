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
        case 1:#ADICIONAR

            for i in range(1):

                valor = input(f"Digite o nome do contato {i + 1}: ")
                nomes.append(valor)

                valor = int(input(f"Digite o telefone do contato {i + 1}: "))
                telefone.append(valor)

                valor = input(f"Digite o email do contato {i + 1}: ")
                email.append(valor)
        case 2:
            #EDITAR

            response = input("Qual o nome do contato que você deseja editar os dados: ")

            if response in nomes: 

                for i in range(1):
                    if nomes[i] == response:
                        posicao = i
            else:
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
        case 3:#EXCLUIR
            
            response = input("Qual o nome do contato que você deseja excluir os dados: ")

            if response in nomes: 

                for i in range(1):
                    if nomes[i] == response:
                        posicao = i
            else:
                print("Nome não está nos seus contatos")
                continue

            print("1 - Excluir Nome\n2 - Excluir telefone\n3 - Excluir Email\n4 - Voltar\n")
            resposta = int(input("Quais parâmetros do contato você deseja editar?"))

            match resposta:
                case 1:
                    nomes[posicao] = ""
                    print(f"Nome do {nomes[posicao]} excluido com sucesso!")
                case 2:
                    telefone[posicao] = 0
                    print(f"Telefone do {nomes[posicao]} excluido com sucesso!")
                case 3:
                    email[posicao] = ""
                    print(f"Email do {nomes[posicao]} excluido com sucesso!")
                case _:
                    continue


        case 4:  # EXIBIR
            # Verificando se há dados para imprimir
            if len(nomes) > 0 and len(telefone) > 0 and len(email) > 0:
                    print("\nContatos")
                    print("=" * 60)  # Linha de separação
                    print(f"{'Nome':<20}{'Telefone':<20}{'Email':<20}")  # Cabeçalho
                    print("-" * 60)  # Linha de separação

                # Imprimindo os contatos apenas se todos os campos tiverem valores
                    for i in range(len(nomes)):
                        if nomes[i] and telefone[i] and email[i]:
                            print(f"{nomes[i]:<20}{telefone[i]:<20}{email[i]:<20}")
        
            else:
                print("Sem dados.")


    if resposta == 5:
        break
