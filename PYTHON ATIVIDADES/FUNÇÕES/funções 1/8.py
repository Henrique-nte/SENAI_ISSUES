#Baseie-se na série de Fibonacci formada pela sequência: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, etc.
#Desenvolver uma estrutura
#modular com uma função que recebe através de parâmetro um número indicando a posição do termo
# e retorna o
#valor correspondente na sequência de Fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  
    


