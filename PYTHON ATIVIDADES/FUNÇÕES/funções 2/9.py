numero = 9
numero_2 = 6

def produto(numero, numero_2):
  if numero > 0 and numero_2 > 0:
    produto = 0
    
    while not numero <= 0:
      if numero % 2 != 0:
        produto += numero_2
    #Dividir sucessivamente um número por 2
    #até que se obtenha 0 como quociente;
      numero //= 2
    #Paralelamente, dobrar, sucessivamente, o segundo número;
      numero_2 *= 2
  return produto
  
  #Somar os números da segunda coluna que tenham como correspondente na primeira coluna um número 
  # ímpar. O total obtido é o produto procurado.

#A seguir escrever um programa que pergunte ao usuário 10 pares de números e 
# calcule os respectivos produtos, usando a função acima.
pares = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10),
         (11, 12), (13, 14), (15, 16), (17, 18), (19, 20)]

for a, b in pares:
  print(f"Produto de {a} e {b}:",produto(a, b))