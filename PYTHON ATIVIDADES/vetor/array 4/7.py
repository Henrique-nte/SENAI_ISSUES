#Faça um algoritmo que leia o nome, a idade e a altura de 40 pessoas. Ao final, informe:
#    O nome e a altura de cada pessoa.
#    A média de altura do grupo.
#    Quantas pessoas têm mais de 30 anos.

nome = []
idade = []
altura = []
soma = 0
contador = 0

for i in range(2):
    nome_valor = input("Digite seu nome: ")
    idade_valor = int(input("Digite sua idade: "))
    altura_valor = int(input("Digite sua altura: "))

    if idade_valor > 30:
        contador += 1

    soma += altura_valor

    nome.append(nome_valor)
    idade.append(idade_valor)
    altura.append(altura_valor)

media = soma / 2


for i in range(2):
    print(f"Nome da {i + 1} {nome[i]} ")
    print(f"idade da pessoa {i + 1} {idade[i]} ")
    print(f"altura da pessoa {i + 1} {altura[i]} ")

print(f"Média altura grupo: {media}")
print(f"Quantas pessoas tem idade maior que 30: {contador}")