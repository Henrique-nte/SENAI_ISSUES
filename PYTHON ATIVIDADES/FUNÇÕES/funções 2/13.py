#13.Desenvolva uma estrutura modular com a função para
#determinar e retornar o n-ésimo termo da sequência de Fibonacci.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  