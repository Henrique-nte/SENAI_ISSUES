#Fazer um algoritmo para um programa de apostas da LOTO. O algoritmo deverá ler, inicialmente,
#  as cinco dezenas sorteadas e, a seguir, ler várias linhas, uma para cada aposta, contendo:
#Número da aposta;
#Quantidade de dezenas apostadas (no máximo, 10);
#As dezenas apostadas.
#A última linha, que não entrará nos cálculos, conterá o número da aposta igual a zero.
#O algoritmo deverá escrever o número de todas as apostas que tiverem três, quatro ou cinco 
# dezenas sorteadas e, ao final, a quantidade de apostadores que fizeram o temo (três dezenas sorteadas),
#  a quadra (quatro dezenas sorteadas) e a quina (cinco dezenas sorteadas). Neste algoritmo, deverá ser
#  utilizada uma sub-rotina que faça a avaliação do número de pontos de cada aposta. 

def avaliar_aposta(dezenas, apostadas):
  acertos = 0
  for dez in apostadas:
    if dez in dezenas:
      acertos += 1
    
  return acertos

dezenas = []  
for i in range(5):
  dezena = int(input(f"Digite a {i + 1}° dezena: "))
  dezenas.append(dezena)

termo = quadra = quina = 0

while True:
  numero = int(input("Numero da Aposta: "))
  if numero == 0:
    break

  qtda_dezenas = int(input("Quantidade de dezenas (máx 10): "))
  apostadas = []  
  
  for i in range(qtda_dezenas):
    dez = int(input(f"{i + 1}° dezena apostada: "))
    apostadas.append(dez)
    
  #print(f"Para a aposta de numero {numero}\n Dezenas acertadas: {acertos} ")

  acertos = avaliar_aposta(dezenas, apostadas)

  if acertos == 3:
      print(f"Aposta {numero}: Termo")
      termo += 1
  elif acertos == 4:
      print(f"Aposta {numero}: Quadra")
      quadra += 1
  elif acertos == 5:
      print(f"Aposta {numero}: Quina")
      quina += 1


# Resultados finais
print("\n===== RESULTADO FINAL =====")
print(f"Total de termos (3 acertos): {termo}")
print(f"Total de quadras (4 acertos): {quadra}")
print(f"Total de quinas (5 acertos): {quina}")