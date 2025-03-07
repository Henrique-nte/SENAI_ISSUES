#4- Faça um programa em JS que alimente um vetor, com um número de posições definidas pelo usuário. 
#Este vetor deverá armazenar um conjunto de nomes em diferentes posições. Crie um mecanismo para 
#alimentar elementos no vetor e pesquisar por um valor existente.
# ======== MENU ======== 

#2) Pesquisar nome 
#3) Listar todos os nome 
#0) Sair do programa 
#——————– 
#Digite sua escolha:

n = int(input("Quantas posições você deseja: "))
nomes = []

for i in range(n):
    #1) Cadastrar nome 
    valor = input(f"Nome {i}: ")