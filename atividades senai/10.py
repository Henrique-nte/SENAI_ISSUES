#Solicite ao usuário um número inteiro n e exiba uma estrutura em forma de triângulo
#numérico de tamanho n. Cada linha do triângulo deve conter números
#de 1 até o número  da linha. Exemplo para 
#n = 5:

#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

n = int(input("Digite um número inteiro n: "))

for i in range(1, n + 1):
    
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  