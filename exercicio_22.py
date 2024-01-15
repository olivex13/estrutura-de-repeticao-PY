''' 
22 - Altere o programa de cálculo dos números primos, 
informando, caso o número não seja primo, por quais número ele é divisível.
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
        return 'não é primo, divisível por 2'
    else:
        divisores = []
        for i in range(3, int(math.sqrt(numero)) + 1, 2):
            if numero % i == 0:
                divisores.append(i)
        if len(divisores) > 0:	
            return f'não é primo, divisível por {", ".join(map(str, divisores))}'
        else:
            return 'É primo'

numero = int(input('Digite um numero: '))

eh_primo = numero_primo(numero)

print (f'O numero {numero} que foi digitado {eh_primo}')
