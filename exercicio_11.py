'''
11 - Altere o programa anterior para mostrar no final a soma dos números.
'''

print('----------SOMANDO NUMEROS----------'.center(60))
print("")

numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))
soma = 0

for i in range(numero_1, numero_2):
        soma += i
        numeros = list(range (numero_1, numero_2))

    
print(f'Os numeros dentro desse intervalo são: {numeros}')       
print(f'A soma desses numeros são: {soma}')


