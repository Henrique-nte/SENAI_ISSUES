#Gere aleatoriamente uma lista de 4 números diferentes entre 0 e 9. Depois, 
#peça ao usuário para adivinhar a sequência correta e informe quantos números
#ele acertou, mas sem revelar quais.

import random
lista = []
acertou = []
verificador = 0
contador = 0

for i in range(4):
    numeros_aleatorios = random.randint(0, 9)
    lista.append(numeros_aleatorios)

print("São 4 números entre 0 e 9.")


for i in range(len(lista)):
    adivinhar = int(input("Tente adivinhar a sequência: "))

    if adivinhar in lista:
        acertou.append(adivinhar)

        
        if adivinhar in acertou:
            contador += 1

        contador += 1
    elif adivinhar not in lista:
        verificador += 1
    
if verificador == len(lista):
    print("Infelizmente você não acertou nenhuma")
elif contador == len(lista):
        print("Parabéns você acertou todos os números")
else:
    print(f"Você acertou {contador} números")


        