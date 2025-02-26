#19.Identificar o tipo de triângulo
#Peça ao usuário três números e verifique se eles podem formar um triângulo.
# Se sim, verifique se é "Equilátero", "Isósceles" ou "Escaleno".
#"Equilátero" se todos os lados forem iguais
#"Isósceles" se dois lados forem iguais
#"Escaleno" se todos os lados forem diferentes

a = int(input("Digite um primeiro número: "))
b = int(input("Digite um segundo número: "))
c = int(input("Digite um terceiro número: "))

if a == b and b == c:
    print("Equilátero")
elif a != b and b != c:
    print("Escaleno")
else:
    print("Isósceles")
