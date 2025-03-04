estoque = int(input("Número de tamanhos de chinelos no estoque:"))
t = 0
i = 0
j = 0
efetivado = 0

for i in range (estoque):
    t += 1
    quantidade = int(input(f"Quantidade para o tamanho {i + 1}:"))

    if i == t:
        pedidos = int(input("Número de pedidos recebidos pela loja: "))
    
        for j in range(pedidos):
            tamanho_pedido = int(input(f"O tamanho do chinelo do pedido {j + 1}:"))

            if tamanho_pedido == quantidade:
                if quantidade > 0:
                    efetivado += 1
                    quantidade -= 1

print(efetivado)

