'''
14 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares 
e a quantidade de números impares.
'''
print('Calculando numeros'.center(120))
print('-------------------------------'.center(120))

lista = []
impar = 0
par = 0

for i in range(10):
    numero = int(input('Digite um numero inteiro: '))
    lista.append(numero)
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1    


print(f' Os numeros digitados foram: {lista}.  \n Contem {par} numero(s) par(es) e  {impar} numero(s) impar(es)')
