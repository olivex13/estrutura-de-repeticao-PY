'''
25 - Faça um programa que peça para n pessoas a sua idade, 
ao final o programa devera verificar se a média de idade da turma 
varia entre 0 e 25,26 e 60 e maior que 60; 
e então, dizer se a turma é jovem, adulta ou idosa, 
conforme a média calculada.
'''

print('PESQUISA DE IDADE'.center(120))
print('')

idades = []
while True:
    entrada = input('Com quantas pessoas você quer fazer a pesquisa? ')

    if entrada.isdigit():
        contador = int(entrada)
        break
    else:
        print('Por favor, digite um número inteiro válido.')

while len(idades) < contador:
    idade = float(input('Digite a idade: '))
    if 0 <= idade <= 110:
        idades.append(idade)
    else:
        print("Digite uma nota de 0 a 10.")

def calcular_media(idades):
    total = sum(idades)
    media = total / len(idades)
    return media
   
media = calcular_media(idades)

def media_da_turma(media):
    if media >= 0 and media <= 25:
        return 'A turma é jovem.'
    elif media >= 26 and media <= 60:
        return "A turma é Adulta."
    else:
        return "A turma é idosa."
    
faixa_etaria = media_da_turma(media)
print("")
print(f' A média de idade da turma é {media} \n {faixa_etaria}')