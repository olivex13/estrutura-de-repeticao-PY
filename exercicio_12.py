'''
12 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
-             Tabuada de 5:
                5 X 1 = 5
                5 X 2 = 10
                    ...
                5 X 10 = 5
'''

print('TABUADA'.center(120))
print('')

tabuada_numero = int(input("Tabuada de qual numero deseja saber? "))
print(f'Tabuada do {tabuada_numero}')

for i in range(1, 11):
    total = tabuada_numero * i
    print(f"{tabuada_numero} x {i} = {total}")