#Faça uma função, que eleve um número inteiro qualquer a uma potência. O número e a
#potência devem ser fornecidos pelo usuário.

def elevar(numero, potencia):
    numero **= potencia
    return numero

while True:
    num = int(input("Digite um número: "))
    pot = int(input("Digite a potência: "))

    print(elevar(num, pot))