'''
27 - Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos
'''

print('MEDIA DE TURMAS'.center(120))
print('')

turmas = int(input("Digite a quantidade de turmas: "))

media = []
contador = 0

while contador < turmas:
  alunos = int(input("Digite a quantidade de alunos da turma: "))
  if alunos <= 40:
    media.append(alunos)
    contador += 1
  else:
    print("A turma não pode ter mais de 40 alunos")

def calcular_media(media):
  return sum(media) / turmas

media_por_turma = calcular_media(media)

print(f"A média de alunos por turma é: {media_por_turma}")


