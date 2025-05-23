#Jogo de Craps. Faça um programa de implemente um jogo de Craps.
#  O jogador lança um par de dados, obtendo um valor entre 2 e 12.
#  Se, na primeira jogada, você tirar 7 ou 11, você um "natural" 
# e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é 
# chamado de "craps" e você perdeu. Se, na primeira jogada, você
#  fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". Seu objetivo 
# agora é continuar jogando os dados até tirar este número novamente.
#  Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
import random

def jogada():
    dado_one = random.randint(1, 6)
    dado_second = random.randint(1, 6)
    return dado_one + dado_second


print("---WELCOME TO THE CRAPS GAME---")
input("Digite qualquer tecla para começar: ")

play = jogada()
print(f"Soma dados: {play}")

point = 0
if play == 7 or play == 11:
    print("---NATURAL, YOU WIN---")
elif play == 2 or play == 3 or play == 12:
    print("---CRAPS, YOU LOST!!---")
else:
    point = play
    while True:
        point = play
        print("---FASE POINT---")
        input("Digite qualquer tecla para rolar: ")
        game = jogada()
        print(f"Soma dados: {game}")

        if game == point:
            print("---WON!---")
            break
        elif game == 7:
            print("---YOU LOST!---")
            break   