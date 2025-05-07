#2- Escreva um programa que, dado um número de dias “x” como parâmetro,
#  imprima: “Daqui a x dias será dia DIA/MÊS/ANO (DIA DA SEMANA)”. 
# Imprima o ano com 4 dígitos e o dia da semana por extenso. 

from datetime import datetime, timedelta

def data_futura_em_x_dias(x):
  dias_da_semana = ['segunda-feira', 'terça-feira', 'quarta-feira',
                      'quinta-feira', 'sexta-feira', 'sábado', 'domingo']

  hoje = datetime.today()
  futura = hoje + timedelta(days=x)

  dia = futura.day
  mes = futura.month
  ano = futura.year
  indice_dia_semana = futura.weekday()  # 0 é segunda-feira, 6 é domingo

  nome_dia = dias_da_semana[indice_dia_semana]

  print(f'Daqui a {x} dias será dia {dia:02d}/{mes:02d}/{ano} ({nome_dia})')

# Exemplo de uso:
dias = int(input("Digite a quantidade de dias no futuro: "))
data_futura_em_x_dias(dias)

