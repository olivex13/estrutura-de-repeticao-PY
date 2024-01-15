'''
23 - Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
'''
print('Numeros primos'.center(120))
print('--------------'.center(120))

def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def encontrar_primos_e_divisoes(N):
    primos = []
    divisoes = 0
    for numero in range(2, N + 1):
        if eh_primo(numero):
            primos.append(numero)
        divisoes += 1

    return primos, divisoes

N = int(input("Digite um número inteiro N: "))

primos, divisoes = encontrar_primos_e_divisoes(N)

print(f"Números primos entre 1 e {N}: {primos}")

print(f"Número de divisões realizadas: {divisoes}")
