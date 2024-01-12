'''
5 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.
'''

print("----------CALCULANDO A POPULAÇÃO----------".center(120))
print('')

populacao_a = int(input('Digite a População A: '))
print('')
populacao_b = int(input('Digite a População B: '))
print('')

taxa_de_crescimento_a = float(input('Digite a porcentagem anual do crescimento da população A:'))
taxa_de_crescimento_b = float(input('Digite a porcentagem anual do crescimento da população B:'))

percentual_a = taxa_de_crescimento_a / 100
print('')
percentual_b = taxa_de_crescimento_b / 100
print('')
ano = 0

while populacao_a < populacao_b:
    populacao_a = populacao_a * (1 + percentual_a)
    populacao_b = populacao_b * (1 + percentual_b)

    ano += 1

print(f'Vai demorar {ano} anos para a população A superar a população B.')