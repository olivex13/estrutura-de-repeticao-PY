'''
20 - Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes 
e limitando o fatorial a números inteiros positivos e menores que 16.
'''

print('CALCULANDO FATORIAL'.center(120))
print('')

while True:
    numero = int(input('Digite um numero: '))

    if numero >= 0 and numero <= 16: 
        def calcular_fatorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * calcular_fatorial(n-1)
        
        resultado = calcular_fatorial(numero)

        print(f'\nA fatorial do número {numero} é: {resultado}\n')
    
    elif numero < 0:
        print('Saindo do programa.')
        break
    else:
        print('Por favor, insira um número positivo menor que 16.')
