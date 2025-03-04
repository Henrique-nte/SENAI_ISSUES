#Ler 80 números e ao final informar quantos número(s) 
#est(á)ão no intervalo entre 10 (inclusive) e 150 (inclusive)

contador = 0
for i in range(80):

    numero = int(input("Digite um número: "))

    if numero >= 10 and numero <= 150:
        contador += 1

print(f"Estão no intervalo entre  10 e 150 {contador} números.")