#3- Em uma cidade do interior, sabe-se que de janeiro a abril de 1976 (121 dias)
#não ocorreu temperatura inferior a 15o C e nem superior a 40o C. Fazer um 
#programa JS que determine:

#a) A menor temperatura ocorrida 
#b) A maior temperatura ocorrida 
#c) A temperatura média do período

temperaturas = []
menor_temperatura = [float("inf")]
maior_temperatura = [float("-inf")]

for  i in range(15, 41):
    
    temperaturas.append(i)

    if i < menor_temperatura[0]:
        menor_temperatura[0] = i
    
    if i > maior_temperatura[0]:
        maior_temperatura[0] = i

#a) A menor temperatura ocorrida
print(f"Menor temperatura: {menor_temperatura[0]}")

#b) A maior temperatura ocorrida 
print(f"Menor temperatura: {menor_temperatura[0]}")

#c) A temperatura média do período
media = sum(temperaturas) / len(temperaturas)

print(media)
print(f"{temperaturas}")