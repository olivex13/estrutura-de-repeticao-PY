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

print(numr_aluno)