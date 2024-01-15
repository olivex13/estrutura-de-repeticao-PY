'''
19 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''

print('LISTA DE NUMEROS'.center(120))
print('')

lista = []
contador = 0

while contador < 5:
    numero = int(input('Digite um numero: '))
    if numero <= 1000:
        lista.append(numero)
        contador += 1
    else: 
        print('Digite um valor entre 0 e 1000')

def maior_numero(lista):
    numero_maior = 0
    for i in lista: 
        if i >= numero_maior:
            numero_maior = i
    return numero_maior

def menor_numero(lista):
    numero_menor = float('inf')
    for i in lista: 
        if i < numero_menor:
            numero_menor = i
    return numero_menor

def soma_numeros(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

soma = soma_numeros(lista)
numero_maior = maior_numero(lista)
numero_menor = menor_numero(lista)

print(f'''Segue as infomações referente aos numero digitados: 
            SOMA DOS NUMEROS = {soma}
            MAIOR NUMERO = {numero_maior}
            MENOR NUMERO = {numero_menor}''')

