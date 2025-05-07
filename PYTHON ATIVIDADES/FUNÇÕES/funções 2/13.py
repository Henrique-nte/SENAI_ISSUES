#13.Desenvolva uma estrutura modular com a função para
#determinar e retornar o n-ésimo termo da sequência de Fibonacci.

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        temp = a  # Guardamos o valor de 'a' temporariamente
        a = b     # Agora 'a' recebe o valor de 'b'
        b = temp + b  # E 'b' recebe a soma do antigo 'a' com o atual 'b'
    return a

n = int(input("Digite o valor de n: "))
print(f"O {n}º termo da sequência de Fibonacci é {fibonacci(n)}.")