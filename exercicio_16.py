'''
16 - A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.
'''
print('FIBONACCI'.center(120))
print('---------'.center(120))

def fibonacci_limite(limite):
    fibo_serie = [0, 1]
    
    while fibo_serie[-1] + fibo_serie[-2] <= limite:
        proximo_numero = fibo_serie[-1] + fibo_serie[-2]
        fibo_serie.append(proximo_numero)
    
    return fibo_serie

limite = 500

resultado = fibonacci_limite(limite)

print("Série de Fibonacci até que o valor seja maior que 500:", resultado)
