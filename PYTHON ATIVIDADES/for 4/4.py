#Escrever um algoritmo que leia o nome e o sexo de 56 pessoas e informe 
#o nome e se ela é homem ou mulher. No final informe total de homens e de mulheres.
masculino = 0
feminino = 0
for i in range(56):
    nome = input("Digite seu nome: ").lower()
    sexo  = input("Informe seu sexo: ").lower()

    if sexo == 'masculino':
        print(f"{nome} você é homem.")
        masculino += 1
    elif sexo == 'feminino':
        print(f"{nome} você é mulher.")
        feminino += 1

print("Total\n")
print(f"Sexo masculino: {masculino}")
print(f"Sexo feminino: {feminino}")
