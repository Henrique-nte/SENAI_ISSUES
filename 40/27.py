#Você deve criar um programa que classifique a nota de um aluno em uma das 
# categorias. O usuário deve inserir a nota do aluno (de 0 a 10), e 
# o programa deve exibir a categoria da nota.
#As categorias de classificação são:
#A: Para notas entre 9.0 e 10.0.
#B: Para notas entre 7.0 e 8.9.
#C: Para notas entre 5.0 e 6.9.
#D: Para notas entre 3.0 e 4.9.
#E: Para notas entre 0.0 e 2.9.

while True:
  nota = float(input("Nota: "))
  
  match nota:
    #A: Para notas entre 9.0 e 10.0.
    case 9 | 10:
      print("A")
    #B: Para notas entre 7.0 e 8.9.
    case nota if nota >= 7 and nota <= 8.9:
      print("B")
    #C: Para notas entre 5.0 e 6.9.
    case nota if nota >= 5 and nota <= 6.9:
      print("C")
    #D: Para notas entre 3.0 e 4.9.
    case nota if nota >= 3 and nota <= 4.9:
      print("D")
    #E: Para notas entre 0.0 e 2.9.
    case nota if nota >= 0 and nota <= 2.9:
      print("E")
  if not (nota >= 0 and nota <= 10):
    print("Nota inválida.")
