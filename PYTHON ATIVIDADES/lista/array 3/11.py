#11- Você está desenvolvendo um aplicativo de agenda de contatos em JS. Crie um programa que permita ao 
# usuário adicionar, editar, excluir e visualizar contatos em sua agenda. Os contatos devem ser armazenados
# em vetores que incluem nome, número de telefone e email.

nomes = []
telefone = []
email = []

print("1 - Adicionar\n2 - Editar\n3 - Excluir\n4 - Exibir")
resposta = int(input("Digite a operação que você deseja realizar: "))

print("Adicionando contatos")

#ADICIONAR
for i in range(2):

    valor = input(f"Digite o nome do contato {i + 1}: ")
    nomes.append(valor)

    valor = input(f"Digite o telefone do contato {i + 1}: ")
    telefone.append(valor)

    valor = input(f"Digite o email do contato {i + 1}: ")
    email.append(valor)

#EXIBIR
print("\nContatos")
print("=" * 60)  # Linha de separação
print(f"{'Nome':<20}{'Telefone':<20}{'Email':<20}")  # Cabeçalho
print("-" * 60)  # Linha de separação

for i in range(2):
    print(f"{nomes[i]:<20}{telefone[i]:<20}{email[i]:<20}")
