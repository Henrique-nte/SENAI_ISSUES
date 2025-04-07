#2- Faça um programa que percorre uma lista com o seguinte
#formato: [['Brasil', 'Itália', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Itália',
#'Espanha', [7,8]]]. Essa lista indica o número de faltas que cada time fez em
#cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10
#faltas e a Itália fez 9. O programa deve imprimir na tela: a) o total de faltas
#do campeonato b) o time que fez mais faltas c) o time que fez menos faltas.

matriz = [
    ['Brasil', 'Itália', [5, 6]],
    ['Brasil', 'Espanha', [1, 2]],
    ['Itália','Espanha', [2,3]]
]

contador_faltas = 0 
contador = 0
faltas_maior = float("-inf")
faltas_menor = 0
linha_maior = 0
linhas = 0

for linha in matriz:
    for numero in linha[2]:
        linhas += 1
        contador += 1
        contador_faltas += numero
        if contador == 2:
            if contador > faltas_maior:
                faltas_maior = contador
                linha_maior = linhas
                

            contador = 0

#a) o total de faltas do campeonato
total_faltas = contador_faltas
print(total_faltas)

#b) o time que fez mais faltas
print(f"Faltas maior: {faltas_maior}")
print(f"Linha que fez mais falta: {linha_maior}")

#c) o time que fez menos faltas