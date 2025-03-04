#Peça ao usuário uma quantidade N de números e um valor LIMITE. O programa deve calcular a
#média apenas dos números ímpares que sejam maiores que LIMITE.

soma = 0
media = 0
numeros = int(input("N números: "))
limite = int(input("Valor limite: "))
contador = 0
for i in range(numeros):
    n = int(input(f"Digite o número {i + 1}:"))
    if n > limite and n % 2 != 0:
            contador += 1
            soma += n
    
if contador > 0:
    media = soma / contador  
    print(f"Soma: {soma}")
    print(f"Média: {media}")
else:
    print("Nenhum número impar maior que limite encontrado.")