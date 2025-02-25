#Crie um programa que simule uma calculadora simples. 
#O usuário deve informar a operação desejada e os dois números 
#para realizar o cálculo. As operações podem ser: adição, subtração,
# multiplicação e divisão.

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