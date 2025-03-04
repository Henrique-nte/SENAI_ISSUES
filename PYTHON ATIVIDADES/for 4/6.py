#Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião em relação 
#ao filme: ótimo=3, bom=2, regular=1. Faça um programa que receba a idade e a opinião de 15 espectadores e que 
#calcule e mostre:

#A média das idades das pessoas que responderam ótimo
#A quantidade de pessoas que respondeu regular
#A percentagem de pessoas que respondeu bom entre todos os espectadores analisados  

regular = 0
bom = 0
otimo = 0
media_regular = 0
por_bom = 0
media_otimo = 0
contador = 0

for i in range(2):
    idade = int(input("Sua idade: "))

    while True:
        opiniao = int(input("ótimo = 3, bom = 2, regular = 1.\n:")) 
        
        if opiniao != 1 and opiniao != 2 and opiniao != 3:
            continue
        else:

            contador += 1

            match opiniao:
                case 1:
                    regular += 1
                case 2:
                    bom += 1
                case 3:
                    otimo += 1

#A média das idades das pessoas que responderam ótimo
media_otimo /= otimo
print(f"Média ótimo: {media_otimo}")
#A quantidade de pessoas que respondeu regular
media_regular /= regular
print(f"Média regular: {media_regular}")
#A percentagem de pessoas que respondeu bom entre todos os espectadores analisados 
por_bom = (bom / contador) * 100
print(f"Porcentagem de pessoas que responderam bom: {por_bom}")