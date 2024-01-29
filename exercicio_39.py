'''
39 - Faça um programa que leia dez conjuntos de dois valores, 
o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, 
junto com suas alturas.
'''

print('Listando Alunos'.center(60))
print('=' * 60)

numr_aluno = []
altura_aluno = []
contador = 0

while contador < 10:
    aluno = int(input('Digite o numero do aluno: '))
    numr_aluno.append(aluno)
    altura = int(input('Digite a altura do aluno em centimentros: '))
    altura_aluno.append(altura)
    contador += 1

aluno_mais_alto = altura_aluno[0]
aluno_mais_baixo = altura_aluno[0]

for i in range(len(altura_aluno)):
    if altura_aluno[i] > aluno_mais_alto:
        aluno_mais_alto = altura_aluno[i]
    elif altura_aluno[i] < aluno_mais_baixo:
        aluno_mais_baixo = altura_aluno[i]

indice_menor_altura = altura_aluno.index(min(altura_aluno))
indice_maior_altura = altura_aluno.index(max(altura_aluno))

print('')
print (f'''O aluno mais alto é o de numero {numr_aluno[indice_maior_altura]} com {altura_aluno[indice_maior_altura]} centimetros. \n
O  aluno mais baixo é o de numero {numr_aluno[indice_menor_altura]} com {altura_aluno[indice_menor_altura]} centimetros.''')