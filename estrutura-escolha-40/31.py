# Peça ao usuário para inserir o valor de um salário bruto e, calcule o imposto a ser pago 
#com base na faixa de rendimento. O programa deve considerar as seguintes faixas de imposto:
#De 0 a 1.000: Isento de imposto.
#De 1.001 a 3.000: Imposto de 10%.
#De 3.001 a 5.000: Imposto de 15%.
#Acima de 5.000: Imposto de 20%.
#O programa deve exibir o valor do imposto e o salário líquido (salário bruto menos o imposto).
while True:
    salario = float(input("Salario bruto: "))

    match salario:
        case salario if salario >= 0 and salario <= 1000:
            imposto = 0
        case salario if salario >= 1001 and salario <= 3000:
            imposto = salario * 0.10
        case salario if salario >= 3001 and salario <= 5000:
            imposto = salario * 0.15
        case salario if salario > 5000:
            imposto = salario * 0.20
    total = salario - imposto
    print(f"Imposto {imposto}")
    print(f"Salario líquido {total}")