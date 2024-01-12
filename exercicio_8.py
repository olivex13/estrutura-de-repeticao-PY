'''
8 - Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

print('----------LENDO NUMEROS----------'.center(120))
print("")

soma = 0

for i in range(5):
    numero = int(input('Digite um numero: '))
    soma += numero

media = soma / 5

print (f'A soma dos numeros digitados é: {soma} e a média é {media}')