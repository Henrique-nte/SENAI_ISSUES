#Crie uma função que receba dois parâmetros: o valor total de uma venda e
#a alíquota de imposto (em
#porcentagem). A função deve retornar o valor do imposto a ser pago.
#● No programa principal, solicite ao usuário o valor de 10 vendas e a
# alíquota e exiba o valor do imposto
#calculado.

def imposto(total, porcentagem):
    imposto = total * (porcentagem / 100)
    return f"Imposto: {imposto}"

for i in range(10):
    valor = float(input(f"Valor da venda {i + 1}: "))
    valor += valor

aliquota = float(input("Alíquota: "))
print(imposto(valor, aliquota))