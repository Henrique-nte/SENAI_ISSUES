#37.Simulação de um caixa eletrônico
#Solicite ao usuário o valor de um saque e verifique quantas notas de 100, 50, 20, 10 e 5 ele receberá.
n100 = 0
n50 = 0
n20 = 0
n5 = 0

valor = int(input("Digite um valor para o saque: "))

n100 = valor // 100
valor %= 100

n50 = valor // 50
valor %= 50

n10 = valor // 10
valor %= 10

n20 = valor // 20
valor %= 20

n5 = valor // 5


print("NOTAS DE 100: ", n100, "\nNOTAS DE 50: ", n50)
print("NOTAS DE 10: ", n10)
print("NOTAS DE 20: ", n20, "\nNOTAS DE 5: ", n5)



