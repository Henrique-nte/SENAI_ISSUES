#Crie uma estrutura de dados para cadastrar produtos. Cada produto deve
# ter um nome, preço e código único. O sistema deve permitir as 
#seguintes operações:

# Cadastrar um novo produto.
# Exibir todos os produtos cadastrados.
# Buscar um produto pelo código.

nomes = []
precos = []
codigos = []



while True:
    print("1 - CADASTRAR NOVO PRODUTO")
    print("2 - EXIBIR TODOS OS PRODUTOS")
    print("3 - BUSCAR PRODUTO PELO CODIGO")
    print("4 - SAIR")
    escolha = int(input("Escolha uma opção: "))

    match escolha:
        case 1:
            for i in range(1):


                nome = input("Nome do produto:")
                preco = input("Preço do produto:")
                codigo = input("Codigo do produto:")

                

                if codigo in codigos:
                    print("Codigo ja existente.")
                    continue
                else:
                    nomes.append(nome)
                    precos.append(preco)
                    codigos.append(codigo)


        case 2:
            for i in range(len(nomes)):
                print(f"Nome do produto {i + 1}: {nomes[i]}")
                print(f"Preço do produto {i + 1}: {precos[i]}")
                print(f"Código do produto {i + 1}: {codigos[i]}")

        case 3: 
            opcao = int(input("Codigo do produto: "))
            
            if codigo in codigos:
                for i in range(len(nomes)):
                    if codigos[i] == codigo:
                        print(nomes[i])
                        print(precos[i])
                        print(codigos[i])
            else:
                print("Produto não cadastrado")
        case 4:
            break