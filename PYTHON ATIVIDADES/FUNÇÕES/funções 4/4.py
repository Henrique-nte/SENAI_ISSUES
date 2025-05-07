#Reverso do número. Faça uma função que retorne o reverso de 
# um número inteiro informado. Por exemplo: 127 -> 721.

def inverter(inteiro):
    invertida = ''

    for i in range(len(inteiro) -1, -1, -1):
        invertida += inteiro[i]

    return invertida

sentence = 127

print(inverter(str(sentence)))