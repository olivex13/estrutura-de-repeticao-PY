'''
17 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
-             Ex.: 5!=5.4.3.2.1=120
'''

print('CALCULANDO FATORIAL'.center(120))
print('')

print('CALCULANDO FATORIAL'.center(120))
print('')

numero = int(input('Digite um numero: '))

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n-1)


resultado = calcular_fatorial(numero)

print(f'''A fatorial no numero {numero} é:
            {resultado}''')
numero = int(input('Digite um numero: '))

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n-1)


resultado = calcular_fatorial(numero)

print(f'''A fatorial no numero {numero} é:
            {resultado}''')
