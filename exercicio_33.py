'''
33 - O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um 
conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, 
bem como a média das temperaturas.
'''

print('Departamento Estadual de Meteorologia Python'.center(60))
print('=' * 60)

temperaturas = []

while True:
    temp_digitada = input('Digite a temperatura ou SAIR para encerrar o programa: ').lower()
    if temp_digitada != 'sair':
        temperaturas.append(float(temp_digitada))
    else:
        break


def menor_temperatura(temperaturas):
    menor_temp = temperaturas[0]
    for i in temperaturas:
        if i < menor_temp:
            menor_temp = i
    return menor_temp

def maior_temperatura(temperaturas):
    maior_temp = temperaturas[0]
    for i in temperaturas:
        if i > maior_temp:
            maior_temp = i
    return maior_temp

def media_temperatura(temperaturas):
    total = sum(temperaturas)
    divisor = len(temperaturas)
    media = total / divisor
    return media


menor_temp = menor_temperatura(temperaturas)
media_temp = media_temperatura(temperaturas)
maior_temp = maior_temperatura(temperaturas)


print(f''' A maior temperatura digitada foi: {maior_temp}
        A menor temperatura digitada foi: {menor_temp}
        A média das temperaturas é:  {media_temp}
      ''')