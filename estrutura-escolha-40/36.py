#Ordenação de três números
#Solicite três números e ordene-os em ordem crescente utilizando apenas estruturas de condição.
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
at = 0
bt = 0
ct = 0

if a > b:
    at = a
    bt = b
    b = at
    a = bt

if b > c:
    bt = b
    ct = c
    c = bt
    b = ct

if a > b:
    at = a
    bt = b
    b = at
    a = bt
print("Números em ordem crescente:", a, b, c)




