'''
35 - Encontrar números primos é uma tarefa difícil. 
Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
'''

import math

print('Numeros primos'.center(60))
print('=' * 60)

def eh_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(numero)) + 1, 2):
            if numero % i == 0:
                return False
        return True

limite_superior = int(input('Digite um número inteiro para o limite superior: '))

numeros_primos = [num for num in range(1, limite_superior + 1) if eh_primo(num)]

print(f'Números primos entre 1 e {limite_superior}: {numeros_primos}')