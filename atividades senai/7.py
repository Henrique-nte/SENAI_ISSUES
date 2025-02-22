# 7 - Crie um programa que solicite números ao usuário 
# continuamente até que ele insira um número negativo. 
# Em seguida, exiba a média dos números positivos fornecidos.
soma = 0
contador = 0
media = 0

while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        break
    if numero > 0:  # Não precisa do "elif" aqui
        soma += numero
        contador += 1

if contador > 0:
    media = soma / contador
    print(f"Média dos números positivos: {media:.2f}")
else:
    print("Nenhum número positivo foi fornecido.")
