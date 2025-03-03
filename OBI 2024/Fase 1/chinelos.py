estoque = int(input("Número de tamanhos de chinelos no estoque:"))
i = 0
while i < estoque:
    
    i += 1
    quantidade = int(input(f"Quantidade para o tamanho {i}:"))
    if i != estoque:
        continue
    pedidos = int(input("Número de pedidos recebidos pela loja: "))
    j = 0
    while j < pedidos:
        j +=1
        efetivado = 0

        tamanho_pedido = int(input(f"O tamanho do chinelo do pedido {j}:"))
        
        if tamanho_pedido == quantidade:
            efetivado += 1
    if j == pedidos:
        break

print(efetivado)