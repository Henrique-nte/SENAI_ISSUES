#Crie uma função que receba o raio como parâmetro e retorne a área do círculo.
# Em seguida, solicite ao
#usuário o valor do raio e exiba o resultado.

def area(raio):
    area = 3.14 * (raio * raio)
    return area

ray = float(input("Digite o raio do círculo: "))    
print(area(ray))