#33 - Ano de eleição
#Solicite o ano de nascimento de uma pessoa e verifique se ela já pode votar.
# A idade mínima para votar é 16 anos, mas a pessoa só é obrigada a 
#votar a partir de 18 anos.

while True:
    nascimento = int(input("Ano de nascimento: "))

    nascimento = 2025 - nascimento

    print(nascimento)
    match nascimento:
        case nascimento if nascimento >= 16 and nascimento < 18:
            print("Você ja pode votar mas não é obrigado.")
        case nasciento if nascimento >= 18:
            print("Você é obrigado a votar.")
        case _:
            print("Você não pode votar.")