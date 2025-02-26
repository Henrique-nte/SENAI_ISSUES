#Conversor de unidades de temperatura
#Solicite ao usuário um valor em Celsius e permita que ele 
#escolha converter para Fahrenheit ou Kelvin.


while True:
    celsius = float(input("Digite a temperatura em celsius: "))

    print("F para converter para Fahrenheit\nK para converter para Kelvin\n:")
    escolha = input("Escolha uma opção: ").lower()
    f = 0
    k = 0
    match escolha:
        case 'f':
            f = celsius * (1.8 + 32)
            print(f"{celsius} em Fahrenheit é {f}")
        case 'k':
            k = celsius + 273
            print(f"{celsius} em Kelvin é {k}")
    

