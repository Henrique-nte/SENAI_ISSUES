efetivado = 0
estoque = []

numero = int(input("Número de tamanhos de chinelos no estoque:"))

for i in range (numero):
    quantidade = int(input(f"Quantidade para o tamanho {i + 1}:"))
    estoque.append(quantidade)

pedidos = int(input("Número de pedidos recebidos pela loja: "))

for i in range(pedidos):
    tamanho_pedido = int(input(f"O tamanho do chinelo do pedido {i + 1}:"))

    if tamanho_pedido in estoque:
        efetivado += 1
        del estoque[tamanho_pedido]

      
print(efetivado)

