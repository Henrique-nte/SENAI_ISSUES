#O usuário insere um número X e um número LIMITE. O programa deve exibir a tabuada de X até o LIMITE.
x = int(input("Você quer saber a tabuada de qual número: "))
limite = int(input("Qual o limite?: "))
i = 0
total = 0

for i in range(limite):
    i += 1
    total = x * i
    print(x, "X", i, "=", total)