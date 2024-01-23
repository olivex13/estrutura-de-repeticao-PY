'''
34 - Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
'''
import math

print('Numeros primos'.center(120))
print('--------------'.center(120))

def numero_primo(numero):
    if numero <= 1:
        return 'não é primo'
    elif numero == 2:
        return 'é primo'
    elif numero % 2 == 0:
        return 'não é primo'
    else:
        for i in range(3, int(math.sqrt(numero)) + 1, 2):
            if numero % i == 0:
                return 'não é primo'
        return 'É primo'

numero = int(input('Digite um numero: '))

eh_primo = numero_primo(numero)

print (f'O numero {numero} que foi digitado {eh_primo}')