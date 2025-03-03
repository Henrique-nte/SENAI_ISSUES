estoque = int(input("Número de tamanhos de chinelos no estoque:"))


for i in range(estoque):
    i += 1
    quantidade = int(input(f"Quantidade para o tamanho {i}:"))

pedidos = int(input("Número de pedidos recebidos pela loja: "))

for i in range (pedidos):
    i += 1
    tamanho_pedido = int(input(f"O tamanho do chinelo do pedido {i}:"))