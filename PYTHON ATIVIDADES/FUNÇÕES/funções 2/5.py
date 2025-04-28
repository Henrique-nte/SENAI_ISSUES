#Desenvolva uma estrutura modular que imprima os números primos
#compreendidos entre 10 e 100. Implemente uma função que
#verifica se um dado número é primo ou não.

import math

def primos():
  i = 10
  while i <= 100:
    j = 2
    while j <= math.sqrt(i):
        if i % j == 0:
            break
        j += 1
    else:
        print(i)  
    i += 1
    
primos()