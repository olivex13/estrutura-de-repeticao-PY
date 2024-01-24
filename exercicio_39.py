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
    altura = float(input('Digite a altura do aluno: '))
    altura_aluno.append(altura)
    contador += 1

aluno_mais_alto = altura_aluno[0]
aluno_mais_baixo = altura_aluno[0]

for i in range(altura_aluno):
    if i >= aluno_mais_alto:
        aluno_mais_alto = i
    elif i <= aluno_mais_baixo:
        aluno_mais_baixo = i

indice_menor_altura = altura_aluno.index(min(altura_aluno))
indice_maior_altura = altura_aluno.index(max(altura_aluno))

print (f'''O aluno mais alto é
''')