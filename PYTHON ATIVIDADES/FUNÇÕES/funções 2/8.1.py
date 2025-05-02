#O número 3025 possui a seguinte característica:
#30 + 25 = 55
#55 * 55 = 3025
#Desenvolva uma estrutura modular que verifica, através de uma função, e imprima todos
# os números de quatro algarismos (de 1000 até 9999) que apresentam tal característica.

def numeros_especiais(numero):
  two_primeiros = numero // 100
  two_ultimos = numero % 100
  soma = two_primeiros + two_ultimos

  if soma * soma == numero:
     print(numero)

for i in range(1000, 9999):
    numeros_especiais(i)