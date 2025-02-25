#21.	Calculadora simples
#Peça para o usuário escolher uma operação (soma, subtração, multiplicação, divisão)
# e dois números. Realize a operação e mostre o resultado.

operacao = input("Digite '+' para adição \nDigite '-' para subtração \nDigite '*' para multiplição\nDigite '/' para divisão\n:")
num1 = float(input("Digite um primeiro valor: "))
num2 = float(input("Digite um segundo valor: "))
resultado = 0
match operacao:
    case '+':
       resultado = num1 + num2
    case '-':
       resultado = num1 - num2
    case '*':
       resultado = num1 * num2
    case '/':
       resultado = num1 / num2
    case _:
        print("Opção inválida.")

print("Resultado: ", resultado)