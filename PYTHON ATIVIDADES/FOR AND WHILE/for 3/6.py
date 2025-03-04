#Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma certa cidade, em um determinado dia.
#Para cada casa visitada foi fornecido o número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo 
#a ele naquela casa. Se a televisão estivesse desligada, nada seria anotado, ou seja, esta casa não entraria na pesquisa.
#Faça um Programa que: 

#leia um número indeterminado de dados, isto é, o número do canal e o número de pessoas que estavam assistindo; 
#calcule e imprima a porcentagem de audiência em cada canal. Para encerrar a entrada de dados, digite o número do canal zero.

canal_4 = 0
canal_5 = 0
canal_7 = 0
canal_12 = 0
soma_assistindo_4 = 0
soma_assistindo_5 = 0
soma_assistindo_7 = 0
soma_assistindo_12 = 0

soma_total = 0
print("1 para sim e 0 para não")
tv = int(input("Sua TV está ligada?"))

while True:
    print("CANAIS\n4, 5, 7, 12")
    canal = int(input("Digite o número do canal (ou 0 para encerrar): "))
    
    if canal == 0:
        print("Encerrando...")
        break
    
    assistindo = int(input("Número de pessoas assistindo: "))
    soma_total += assistindo
    
    match canal:
        case 4:
            canal_4 += 1
            soma_assistindo_4 += assistindo
        case 5:
            canal_5 += 1
            soma_assistindo_5 += assistindo
        case 7:
            canal_7 += 1
            soma_assistindo_7 += assistindo
        case 12:
            canal_12 += 1
            soma_assistindo_12 += assistindo
        case _:
            print("Canal inválido.")
        
if soma_total > 0:
    porcentagem_4 = (soma_assistindo_4 * 100) / soma_total
    porcentagem_5 = (soma_assistindo_5 * 100) / soma_total
    porcentagem_7 = (soma_assistindo_7 * 100) / soma_total
    porcentagem_12 = (soma_assistindo_12 * 100) / soma_total
        
    
print(f"O canal 4 teve {porcentagem_4:.2f}% de audiência.")
print(f"O canal 5 teve {porcentagem_5:.2f}% de audiência.")
print(f"O canal 7 teve {porcentagem_7:.2f}% de audiência.")
print(f"O canal 12 teve {porcentagem_12:.2f}% de audiência.")
        
    
    