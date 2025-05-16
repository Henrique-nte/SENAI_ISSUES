#Crie uma função que receba o raio como parâmetro e retorne a área do círculo.
# Em seguida, solicite ao
#usuário o valor do raio e exiba o resultado.

def area(raio):
    area = 3.14 * (raio * raio)
    return f"Área do circulo: {area}"

ray = float(input("Digite o valor do raio: "))    
print(area(ray))