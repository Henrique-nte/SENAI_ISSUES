#4- Faça um programa em JS que alimente um vetor, com um número de posições definidas pelo usuário. 
#Este vetor deverá armazenar um conjunto de nomes em diferentes posições. Crie um mecanismo para 
#alimentar elementos no vetor e pesquisar por um valor existente.
# ======== MENU ======== 
#1) Cadastrar nome 
#2) Pesquisar nome 
#3) Listar todos os nome 
#0) Sair do programa 
#——————– 
#Digite sua escolha:


nomes = []
i = 0
while True:
    
    print("======== MENU ========")
    print(" (1) Cadastrar nome") 
    print(" (2) Pesquisar nome")
    print(" (3) Listar todos os nomes")
    print(" (0) Sair do programa")
    escolha = int(input("Digite sua escolha: "))

    if escolha == 0:
        #0) Sair do programa 
        break

    elif escolha == 1:
        
        #1) Cadastrar nome
        valor = input(f"Nome {i + 1}: ")
        nomes.append(valor)
        i += 1

    elif escolha == 2:
        #2) Pesquisar nome
        nome_procurar = input("Nome que você deseja procurar: ")
        if nome_procurar in nomes:
            print(f"O nome {nome_procurar} está na lista")
        else:
            print(f"O nome {nome_procurar} não está na lista")

    elif escolha == 3:
        #3) Listar todos os nome 
        print(nomes)
    
    