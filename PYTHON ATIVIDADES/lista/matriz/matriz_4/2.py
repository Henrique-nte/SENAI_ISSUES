#2- Faça um programa que percorre uma lista com o seguinte
#formato: [['Brasil', 'Itália', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Itália',
#'Espanha', [7,8]]]. Essa lista indica o número de faltas que cada time fez em
#cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10
#faltas e a Itália fez 9. O programa deve imprimir na tela: a) o total de faltas
#do campeonato b) o time que fez mais faltas c) o time que fez menos faltas.

matriz = [

    ['Brasil', 'Itália', [1, 5]],
    ['Brasil', 'Espanha', [2, 5]],
    ['Itália','Espanha', [3, 5]]

]

#b) o time que fez mais faltas
for i in range(len(matriz)):
    for j in range(matriz[i][2]):
        print(matriz[i][j])


contador_faltas = 0 
contador_faltas_total = 0
contador = 0
faltas_maior = float("-inf")
faltas_menor = 0
linha_maior = 0
linhas = 0

for linha in matriz:
    for numero in linha[2]:
        contador_faltas_total += numero

#a) O total de faltas do campeonato
total_faltas = contador_faltas_total
print(contador_faltas_total)


        

#c) o time que fez menos faltas