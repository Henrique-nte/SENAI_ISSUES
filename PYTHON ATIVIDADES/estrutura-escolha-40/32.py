#32. Peça ao usuário para inserir um número inteiro positivo e verifique se ele é um quadrado perfeito.
# Um número é considerado um quadrado perfeito quando existe um
#número inteiro xxx tal que x×x=nx \times x = nx×x=n, onde nnn é o número fornecido. Por exemplo:
#●	161616 é um quadrado perfeito porque 4×4=164 \times 4 = 164×4=16.
#●	252525 é um quadrado perfeito porque 5×5=255 \times 5 = 255×5=25.
#●	141414 não é um quadrado perfeito porque não há um número inteiro que, multiplicado por si mesmo,
# resulte em 141414.

import math
while True:
    numero = int(input("Digite um número inteiro positivo: "))

    if (numero < 0 or numero == 0):
        print("Número inválido.")
    elif numero == 0:
        print("Número inválido. Zero não é considerado um quadrado perfeito.")
    else:
        break  # Sai do loop se o número for válido
    if not (numero < 0 or numero == 0):
        break

n = numero
raiz = math.sqrt(n)

if raiz == int(raiz):
    if (raiz * n) == numero:
        print(f"{numero} é um quadrado perfeito.")
    else:
        print(f"{numero} não é um quadrado perfeito.")
else:
    print(f"{numero} não é um quadrado perfeito.")



