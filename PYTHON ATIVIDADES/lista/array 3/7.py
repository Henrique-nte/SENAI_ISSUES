#7- Crie um array de números e solicite ao usuário um número. Verifique se esse número 
#existe no array e, em caso afirmativo, exiba a posição onde ele está localizado.

numeros = [1, 2, 3, 4, 5]
i = 0
numero = int(input("Digite um número: "))

for i in range(5):
    if numeros[i] == numero:
        posicao = i
    
if numero in numeros:
    print("Está na lista.")
    print(f"Posição: {posicao + 1}")
else:
    print("Não está na lista.")