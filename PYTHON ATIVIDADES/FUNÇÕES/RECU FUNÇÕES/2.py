#Faça um algoritmo para ler um vetor de 20 números. Após isto, deverá ser lido mais um
#número qualquer e verificar se esse número existe no vetor ou não. Se existir, o
#algoritmo deve gerar um novo vetor sem esse número. (Considere que não haver
#números repetidos no vetor)

def verificar(numero, vetor):
    new_vetor = []
    if numero in vetor:
        encontrado = numero
        
    for i in range(len(vetor)):
        if vetor[i] != encontrado:
            new_vetor.append(vetor[i])
    
    return new_vetor

vet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
num = 5

print(verificar(num, vet))

