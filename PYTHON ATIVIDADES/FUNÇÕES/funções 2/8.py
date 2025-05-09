#O número 3025 possui a seguinte característica:
#30 + 25 = 55
#55 * 55 = 3025
#Desenvolva uma estrutura modular que verifica, através de uma função, e imprima todos
# os números de quatro algarismos (de 1000 até 9999) que apresentam tal característica.
def numeros_especiais(numero):
  two = 0
  for i in range(1, numero):
    if i * i == numero:
      two = i
      
  j = 0
  dois_primeiros = ''

  for i in str(numero):
    if j <= 1:
      dois_primeiros += i
    j +=1 
  
  two_primeiros = int(dois_primeiros)
  
  j = 0
  dois_ultimos = ''

  for i in str(numero):
    if j > 1:
      dois_ultimos += i
    j += 1 

  two_ultimos = int(dois_ultimos)
  
  if two_primeiros + two_ultimos == two and two * two == numero:
    print(numero)

for i in range(1000, 9999):
    numeros_especiais(i)