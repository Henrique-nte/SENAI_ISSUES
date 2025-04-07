#2- Faça um programa que percorre uma lista com o seguinte
#formato: [['Brasil', 'Itália', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Itália',
#'Espanha', [7,8]]]. Essa lista indica o número de faltas que cada time fez em
#cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10
#faltas e a Itália fez 9. O programa deve imprimir na tela: a) o total de faltas
#do campeonato b) o time que fez mais faltas c) o time que fez menos faltas.

matriz = [
    ['Brasil', 'Itália', [10, 9]],
    ['Brasil', 'Espanha', [5, 7]],
    ['Itália','Espanha', [7,8]]
]

contador = 0 

for linha in matriz:
    for numero in linha[2]:
        contador += numero

total_faltas = contador

print(contador)

#a) o total de faltas do campeonato
#b) o time que fez mais faltas
#c) o time que fez menos faltas