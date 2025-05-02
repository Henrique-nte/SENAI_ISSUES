#Desenvolva uma estrutura modular com uma função que recebe dois números inteiros, positivos,
#  e determine o produto dos mesmos, utilizando o seguinte método de multiplicação:
#Dividir sucessivamente o primeiro número por 2 até que se obtenha 0 como quociente;
#Paralelamente, dobrar, sucessivamente, o segundo número;
#Somar os números da segunda coluna que tenham como correspondente na primeira coluna um número 
# ímpar. O total obtido é o produto procurado.
#Exemplo: 9 x 6
#9, ímpar				 6	----> 6
#(4 / 2) = 2, par		24
#(2 / 2) = 1, ímpar		48	----> 48, 6 + 48 = 54
#A seguir escrever um programa que pergunte ao usuário 10 pares de números e calcule 
# os respectivos produtos, usando a função acima.

numero = 9
numero_2 = 6

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

print(produto)
  #Somar os números da segunda coluna que tenham como correspondente na primeira coluna um número 
  # ímpar. O total obtido é o produto procurado.
  