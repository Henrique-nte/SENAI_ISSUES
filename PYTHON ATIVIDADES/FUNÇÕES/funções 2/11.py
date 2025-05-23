#Escrever uma função que faz criptografia por substituição, ou seja, pega um texto legível
#e transforma em texto cifrado, substituindo os caracteres originais por caracteres que
#estão "n" posições na frente. Este processo também é conhecido como “Cifra de César”.
def cifra_de_cesar(texto, chave):

    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
    
    texto_criptografado = ''

    for i in range(len(texto)):
        for j in range(len(alfabeto)):
            if texto[i] == alfabeto[j]:
                texto_criptografado += (alfabeto[j + chave])


    return texto_criptografado

string = "olamundo"
print(f"Original: {string} ")
key = -2

print("Criptografado:", cifra_de_cesar(string, key))
