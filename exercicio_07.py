'''
7 - Faça um programa que leia 5 números e informe o maior número.
'''

print("-----------QUAL É O MAIOR NUMERO?----------".center(120))
print('')

numero_maior = 0

for i in range(5):
    numero = int(input("Digite um numero: "))
    if numero > numero_maior:
        numero_maior = numero

print (f'O maior digitado foi  {numero_maior}')