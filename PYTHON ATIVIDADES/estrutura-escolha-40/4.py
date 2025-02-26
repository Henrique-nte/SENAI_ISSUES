#4.	A concessionária de veículos “CARANGO” está vendendo os seus veículos com desconto. 
#Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente. 
#O desconto deverá ser calculado sobre o valor do veículo de acordo com o combustível 
#(álcool – 25%, gasolina – 21% ou diesel –14%). 

veiculo = float(input("Valor do veículo: "))
tipo = input("Tipo do combustível: ").lower()

match tipo:
    case 'alcool':
        desconto = veiculo * 0.25

    case 'gasolina':
        desconto = veiculo * 0.21

    case 'diesel':
        desconto = veiculo * 0.14
    case _:
        print("opção inválida.")



print("Valor do desconto: ", desconto)
valor = veiculo - desconto
print("Valor total: ", valor)


