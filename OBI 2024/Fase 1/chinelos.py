efetivado = 0
estoque = []

numero = int(input("Número de tamanhos de chinelos no estoque: "))

# Preenchendo o estoque com tamanhos e suas quantidades
for i in range (numero):
    quantidade = int(input(f"Quantidade para o tamanho {i + 1}:"))
    estoque.append(quantidade)

pedidos = int(input("Número de pedidos recebidos pela loja: "))

# Processando pedidos
for _ in range(pedidos):
    tamanho_pedido = int(input("Tamanho do chinelo do pedido: "))

    if tamanho_pedido in estoque and estoque[tamanho_pedido] > 0:
        efetivado += 1
        estoque[tamanho_pedido] -= 1  # Reduz a quantidade disponível desse tamanho

print(efetivado)
