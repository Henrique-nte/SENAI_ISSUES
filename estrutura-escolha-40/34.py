#Peça ao usuário para inserir a temperatura em graus Celsius.
#Com base no valor informado, o programa deve classificar a temperatura 
#em uma das seguintes categorias:
#Muito Frio: Menor que 0°C.
#Frio: De 0°C a 15°C.
#Ameno: De 16°C a 25°C.
#Quente: De 26°C a 35°C.
#Muito Quente: Maior que 35°C.

while True:
    celsius = float(input("Temperatura em celsius: "))

    match celsius:
        case celsius if celsius < 0:
            print("Muito Frio")
        case celsius if celsius >= 0 and celsius <= 15:
            print("Frio")
        case celsius if celsius >= 16 and celsius <= 25:
            print("Ameno")
        case celsius if celsius >= 26 and celsius <= 35:
            print("Quente")
        case celsius if celsius > 35:
            print("Muito Quente")
