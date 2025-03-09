efetivado = 0
pedidos = []
estoque = int(input("Número de tamanhos de chinelos no estoque:"))

for i in range (estoque):
    
    quantidade = int(input(f"Quantidade para o tamanho {i + 1}:"))

pedidos = int(input("Número de pedidos recebidos pela loja: "))
pedidos.append(pedidos)

for j in range(pedidos):
    tamanho_pedido = int(input(f"O tamanho do chinelo do pedido {j + 1}:"))

    if tamanho_pedido == estoque[j]:
        efetivado += 1
        pedidos -= estoque[j]

print(efetivado)

