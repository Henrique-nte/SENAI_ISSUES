#15.Verificar se o número é divisível por 3 ou 5
#Solicite um número e imprima "Sim" se ele for divisível por 3 ou por 5, 
#e "Não" caso contrário.

numero = float(input("Digite um número: "))

if numero % 3 == 0 or numero % 5 == 0:
    print("Divisível por 3 ou por 5.")
else:
    print("Não é divisível")
