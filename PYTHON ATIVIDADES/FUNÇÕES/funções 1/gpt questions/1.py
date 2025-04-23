def eh_prefixo(palavra1, palavra2):
    if len(palavra1) > len(palavra2):
        return False
      
    return True

# Exemplo de uso
palavra = "in"
palavra_2 = "inútil"

print(eh_prefixo(palavra, palavra_2))  
