#24.Verificar se é um número primo
#Solicite um número e verifique se ele é primo (divisível apenas por 1 e por ele mesmo)

numero = float(input("Digite um número: "))

if numero % 1 == 0 and numero % numero == 0:
    print("Primo.")
else:
    print("Não é primo.")
