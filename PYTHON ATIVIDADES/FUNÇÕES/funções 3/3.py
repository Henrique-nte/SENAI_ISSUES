#3- Altere o programa do exercício anterior para imprimir o dia da
#semana em uma língua diferente (português, inglês, francês, espanhol, etc.).

from datetime import datetime, timedelta

def obter_dia_em_idioma(indice, idioma):
    dias = {
        'pt': ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo'],
        'en': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'fr': ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche'],
        'es': ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    }
    return dias.get(idioma, dias['pt'])[indice]

def data_futura_em_x_dias(x, idioma='pt'):
    hoje = datetime.today()
    futura = hoje + timedelta(days=x)

    dia = futura.day
    mes = futura.month
    ano = futura.year
    indice_dia_semana = futura.weekday()  

    nome_dia = obter_dia_em_idioma(indice_dia_semana, idioma)

    print(f'Daqui a {x} dias será dia {dia:02d}/{mes:02d}/{ano} ({nome_dia})')


dias = int(input("Digite a quantidade de dias no futuro: "))
idioma = input("Escolha o idioma (pt, en, fr, es): ").strip().lower()
data_futura_em_x_dias(dias, idioma)
