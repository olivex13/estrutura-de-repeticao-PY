'''
24 - Faça um programa que calcule o mostre a média aritmética de N notas.
'''

print('CALCULADORA DE MÉDIA'.center(120))
print('')

notas = []
while True:
    entrada = input('Quantas notas você tem para calcular? ')

    if entrada.isdigit():
        contador = int(entrada)
        break
    else:
        print('Por favor, digite um número inteiro válido.')

while len(notas) < contador:
    nota = float(input('Digite a nota: '))
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Digite uma nota de 0 a 10.")

def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

   
media = calcular_media(notas)

print(f' A média refernete as notas digitadas é {media}')


