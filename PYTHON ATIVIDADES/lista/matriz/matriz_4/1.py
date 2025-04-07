perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?",
"Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

contador = 0
print("1 - SIM")
print("2 - NÃO")

for i in range(len(perguntas)):
    print(perguntas[i])
    resposta = int(input(""))
    if resposta == 1:
        contador += 1

match contador:
    case 0:       
        clasificacao = "inocente"
    case 2:
        clasificacao = "suspeito"
    case contador if contador >= 3 and contador <= 4:
        clasificacao = "cúmplice"
    case 5:
        clasificacao = "assassino"

print(f"Você é: {clasificacao}")