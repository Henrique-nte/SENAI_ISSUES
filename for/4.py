# Deseja-se fazer uma pesquisa sobre o consumo mensal de energia elétrica em uma determinada cidade.
# Dados fornecidos:
# - Preço do kWh consumido;
# - Número do consumidor;
# - Quantidade de kWh consumidos durante o mês;
# - Código do tipo de consumidor (residencial = R, comercial = C, industrial = I).
# O número do consumidor igual a zero deve ser usado como finalizador da aplicação.

maior_consumo = 0
menor_consumo = float('inf')  # Inicializa com um valor muito alto para comparar
total_consumo = 0
contador = 0
total_consumo_residencial = 0
total_consumo_comercial = 0
total_consumo_industrial = 0
soma_consumo = 0

# Variáveis para armazenar os tipos de maior e menor consumo
tipo_maior_consumo = ""
tipo_menor_consumo = ""

while True:
    try:
        codigo = input("Código do tipo de consumidor (residencial = R, comercial = C, industrial = I): ").lower()
        if codigo == "0":
            break  # Finaliza a aplicação quando o código é 0

        # Verificação do tipo de consumidor
        if codigo == "r":
            tipo = "Residencial"
        elif codigo == "c":
            tipo = "Comercial"
        elif codigo == "i":
            tipo = "Industrial"
        else:
            print("Código inválido! Tente novamente.")
            continue

        numero = int(input("Número do consumidor: "))
        if numero == 0:
            print("Número inválido. Finalizando aplicação.")
            break

        preco = float(input("Preço do KWh consumido: "))
        quantidade = int(input("Quantidade de kWh consumidos durante o mês: "))

        total = preco * quantidade  # Total a pagar
        contador += 1
        soma_consumo += quantidade

        # a) Exibe o total a pagar para o consumidor
        print(f"Para o consumidor {numero}, o total a pagar é: R${total:.2f}")

        # b) Maior consumo verificado
        if quantidade > maior_consumo:
            maior_consumo = quantidade
            tipo_maior_consumo = tipo

        # c) Menor consumo verificado
        if quantidade < menor_consumo:
            menor_consumo = quantidade
            tipo_menor_consumo = tipo

        # d) Total de consumo por tipo de consumidor
        if codigo == 'r':
            total_consumo_residencial += quantidade
        elif codigo == 'c':
            total_consumo_comercial += quantidade
        elif codigo == 'i':
            total_consumo_industrial += quantidade

    except ValueError:
        print("Entrada inválida! Certifique-se de digitar números corretamente.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# e) Média geral de consumo
if contador > 0:
    media_geral_consumo = soma_consumo / contador
else:
    media_geral_consumo = 0

# Exibindo os resultados finais
print("\n--- Resultados Finais ---")
print(f"Maior consumo: {maior_consumo} kWh (Tipo: {tipo_maior_consumo})")
print(f"Menor consumo: {menor_consumo} kWh (Tipo: {tipo_menor_consumo})")
print(f"Consumo total Residencial: {total_consumo_residencial} kWh")
print(f"Consumo total Comercial: {total_consumo_comercial} kWh")
print(f"Consumo total Industrial: {total_consumo_industrial} kWh")
print(f"Média geral de consumo: {media_geral_consumo:.2f} kWh")
