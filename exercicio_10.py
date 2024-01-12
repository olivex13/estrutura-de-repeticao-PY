'''
10 - Faça um programa que receba dois números inteiros 
e gere os números inteiros que estão no intervalo compreendido por eles.
'''

print('----------NUMEROS INTEIROS----------'.center(60))
print("")

numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))

for i in range(numero_1, numero_2):
        print(i)