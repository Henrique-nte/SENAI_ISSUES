#22 - Você deve criar um programa que classifique o nível de acesso de um usuário com base na sua função.
# O usuário deve inserir o nome de sua função, e o programa deve indicar qual é o seu nível de acesso.
#As funções e seus níveis de acesso são:
#●	Admin: Nível de acesso 3 (Acesso completo).
#●	Gerente: Nível de acesso 2 (Acesso limitado, mas pode gerenciar usuários).
#●	Funcionário: Nível de acesso 1 (Acesso restrito, apenas pode consultar informações).

print("'adm' para Admin 'ger' para gerente 'fun' para funcionario")
funcao = input("Sua função: ").lower()

match funcao:
    case 'adm':
        print("Acesso completo")
    case 'ger':
        print("Acesso limitado, mas pode gerenciar usuários")
    case 'fun':
        print("Acesso restrito, apenas pode consultar informações")

