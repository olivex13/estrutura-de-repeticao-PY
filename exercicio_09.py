'''
9 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''

print("----------NUMEROS IMPARES----------")
print('')

for i in range(1, 51):
    if i % 2 != 0:
        print(i)
        