#Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião em relação 
#ao filme: ótimo=3, bom=2, regular=1. Faça um programa que receba a idade e a opinião de 15 espectadores e que 
#calcule e mostre:
#A média das idades das pessoas que responderam ótimo
#A quantidade de pessoas que respondeu regular
#A percentagem de pessoas que respondeu bom entre todos os espectadores analisados  

regular = 0
bom = 0
otimo = 0

por_bom = 0
media_otimo = 0
contador = 0
idade_otimo = 0


for i in range(5):
    contador += 1
    idade = int(input("Sua idade: "))
    opiniao = int(input("ótimo = 3, bom = 2, regular = 1.\n:"))

    match opiniao:
        case 1:
            regular += 1
        case 2: 
            bom += 1
        case 3:
            idade_otimo += idade
            otimo += 1
    

#A média das idades das pessoas que responderam ótimo
media_otimo = idade_otimo / contador
print(f"A média das idades das pessoas que responderam ótimo: {media_otimo}")
#A quantidade de pessoas que respondeu regular
print(f"A quantidade de pessoas que respondeu regular: {regular}")
#A percentagem de pessoas que respondeu bom entre todos os espectadores analisados 
por_bom = (bom / contador) * 100
print(f"Porcentagem de pessoas que responderam bom: {por_bom}")