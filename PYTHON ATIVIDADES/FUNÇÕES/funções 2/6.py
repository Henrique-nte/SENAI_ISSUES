#6 - Número perfeito é aquele cuja soma de seus divisores, exceto ele próprio,
#é igual ao número. Exemplo: 6 é perfeito porque 1 + 2 + 3 = 6. 
#Desenvolva uma estrutura modular que imprima os números perfeitos
#compreendidos entre 1 e 500.
def perfect():
    perfeitos = []
    for i in range(1, 500):
        j = 1
        divisores = []
        resul = 0
        while i > j:
            if i % j == 0:
                divisores.append(j)
            j += 1
        for k in divisores:
            resul += k

        if resul == i:
            perfeitos.append(i)

    return perfeitos        
        
        
print(perfect())