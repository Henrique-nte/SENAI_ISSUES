#1- Faça um menu para que o usuário opte por  (1) – Somar  (2) – Subtrair  (3) – Multiplicar  (0) - Sair 2. 
#Prossiga com o programa, adicionando valores as matrizes A e B e calculando:  A soma das matrizes A e B, 
#colocando o resultado na matrizSom.  A subtração das matrizes A e B, colocando o resultado na matrizSub. 
#A multiplicação das matrizes A e B, colocando o resultado na matrizMul.  
#Obs: o tamanho das matrizes Sub,
# Som e Mul será automaticamente programável. Uma vez que o programa sabe qual o número de linhas da matriz
# A e B e qual o número de colunas da matriz A e B, automaticamente se saberá qual o tamanho da matriz resultante
# nos passos anteriores isso já foi feito

a = []
b = []

#Soma da matriz A e B
matrizSom = []
#Subitração da matriz A e B
matrizSub = []
#Multiplicacção da matriz A e B
matrizMul = []



print("Matriz A")
for linha in range(2):
    linha = []
    for coluna in range(3):
        valor = float(input("Digite o valor da venda: "))
        linha.append(valor)
    a.append(linha)
print(a)

print("Matriz B")
for linha in range(2):
    linha = []
    for coluna in range(3):
        valor = float(input("Digite o valor da venda: "))
        linha.append(valor)
    b.append(linha)
print(b)

while True:
    print("1 - SOMAR")
    print("2 - SUBTRAIR")
    print("3 - MULTIPLICAR")
    print("0 - SAIR")
    escolha = int(input("Escolha uma opção: "))
    if escolha == 0:
        break
    elif escolha != 1 and escolha != 2 and escolha != 3:
        print("Opção inválida.")
        continue

    match escolha:
        case 1: 
            for i in range(len(a)):  # Percorre as linhas
                linha = []
                for j in range(len(a[0])):  # Percorre as colunas
                    linha.append(a[i][j] + b[i][j])  # Soma os elementos na mesma posição
                matrizSom.append(linha)

            print(f"Soma Matriz A e B: {matrizSom}")
        case 2:
            for i in range(len(a)):  # Percorre as linhas
                linha = []
                for j in range(len(a[0])):  # Percorre as colunas
                    linha.append(a[i][j] - b[i][j])  # Subtrai os elementos na mesma posição
                matrizSub.append(linha)

            print(f"Soma Matriz A e B: {matrizSub}")
        case 3:
            for i in range(len(a)):  # Percorre as linhas
                linha = []
                for j in range(len(a[0])):  # Percorre as colunas
                    linha.append(a[i][j] * b[i][j])  # Multiplica os elementos na mesma posição
                matrizMul.append(linha)

            print(f"Soma Matriz A e B: {matrizMul}")
            
                
                                            


