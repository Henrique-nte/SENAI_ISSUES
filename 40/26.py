#Verificar idade para entrar em evento
#Solicite ao usuário a idade e verifique se ele pode ou não entrar em um evento:
#Menor que 18 anos: "Não autorizado"
#18 anos ou mais: "Autorizado"

idade = int(input("Idade: "))

match idade:
  case idade if idade < 18:
    print("Não autorizado")
  case _:
    print("Autorizado")
