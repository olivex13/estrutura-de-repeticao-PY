'''28 - Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''


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
total = sum(valor_do_cd)

print('')
print('Lista de CDs')

if len(nome_do_cd) == len(valor_do_cd):
  
    for i in range(len(nome_do_cd)):
        print(f"{nome_do_cd[i]} - {valor_do_cd[i]}")
else:
    print("As listas não têm o mesmo comprimento.")

print(f'O valor total investido na coleção foi R$ {total:.2f}')
print(f'O valor médio investido por CD é R$ {media:.2f}')
