#10- Leia nomes de pessoas com seus respectivos telefones, sendo a quantidade determinada pelo 
# usuário. Em seguida, pergunte ao usuário qual o nome que ele deseja consultar o telefone. 
# Após sua resposta, exiba o telefone da pessoa procurada.

nomes = []
telefones = []

n = int(input("Quantas pessoas deseja armazenar: "))

for i in range(n):
  valor = input(f"Digite o nome {i + 1}: ")
  nomes.append(valor)

  valor = int(input(f"Digite o telefone {i + 1}: "))
  telefones.append(valor)

nome = input("Qual o nome deseja consultar o telefone?: ")

for i in range(n):

  if nomes[i] == nome:
    posicao = i
    print(f"Telefone do {nome}: {telefones[posicao]}")
    contador = 1

if contador < 1:
  print("Nome não está na lista.")
    