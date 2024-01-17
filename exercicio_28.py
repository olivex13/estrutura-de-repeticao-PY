'''28 - Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''


print("COLEÇÃO DE CDs".center(120))
print("="*120)

nome_do_cd = []
valor_do_cd = []

contador = int(input("Quantos CDs você tem? "))

for i in range(contador):
  nome_do_cd.append(input("Nome do CD: "))
  valor_do_cd.append(float(input("Valor do CD: ")))

def calcular_media(valor_do_cd, contador):
 media = sum(valor_do_cd) / contador
 return media

media = calcular_media(valor_do_cd, contador)

print(media)