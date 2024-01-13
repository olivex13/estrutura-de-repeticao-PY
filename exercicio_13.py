'''
13 - Faça um programa que peça dois números, base e expoente
calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.
'''

print('Calculando numeros'.center(120))
print('-------------------------------'.center(120))

base = float(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

resultado = 1

for i in range(expoente):
    resultado *= base

print(f"{base} elevado a {expoente} é igual a {resultado}")

