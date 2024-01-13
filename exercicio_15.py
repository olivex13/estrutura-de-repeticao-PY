'''
15 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo.

'''

print('FIBONACCI'.center(120))
print('---------'.center(120))

def fibonacci(n):
    fibo_serie = [1, 1]
    
    for i in range(2, n):
        proximo_numero = fibo_serie[-1] + fibo_serie[-2]
        fibo_serie.append(proximo_numero)
    
    return fibo_serie[:n]

# Solicita o valor de n
n = int(input("Digite o valor de n para a série de Fibonacci: "))

# Gera a série de Fibonacci até o n-ésimo termo
resultado = fibonacci(n)

print(f"Série de Fibonacci até o {n}-ésimo termo:", resultado)
