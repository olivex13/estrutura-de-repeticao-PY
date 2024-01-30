'''
40 - Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:
- Código da cidade;
- Número de veículos de passeio (em 1999);
- Número de acidentes de trânsito com vítimas (em 1999). 
-                    Deseja-se saber:
- Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
- Qual a média de veículos nas cinco cidades juntas;
- Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

'''

print('Acidentes de transito 1999'.center(120))
print('=' * 120)

cidades = []
veiculos = []
acidentes = []
contador = 0

while contador < 5:
    cidade = int(input("Digite o código da cidade: "))
    cidades.append(cidade)
    veiculo = int(input('Digite a quantidade de veículos de passeio: '))
    veiculos.append(veiculo)
    acidente = int(input("Digite a quantidade de acidentes com vítimas: "))
    acidentes.append(acidente)
    contador += 1

maior_acidente = acidentes[0]
menor_acidente = acidentes[0]
indice_menor_acidente = 0
indice_maior_acidente = 0


for i in range(len(acidentes)):
    if acidentes[i] > maior_acidente:
        maior_acidente = acidentes[i]
        indice_maior_acidente = i

    elif acidentes[i] < menor_acidente:
        menor_acidente = acidentes[i]
        indice_menor_acidente = i
media_veiculos = []
media_cidades = []
media_acidentes = []

for i in range(len(veiculos)):
    if veiculos[i] > 2000:
        media_veiculos.append(veiculos[i])
        media_cidades.append(cidades[i])
        media_acidentes.append(acidentes[i])

media_dos_acidentes = sum(media_acidentes) / len(media_cidades)


media_veiculos = sum(veiculos) / 5

print('')
print(f'''A cidade com menor indice de acidente é a de código: {cidades[indice_menor_acidente]}. Com {acidentes[indice_menor_acidente]} acidente(s). \n
A cidade com maior indice de acidente é a de código {cidades[indice_maior_acidente]}. Com {acidentes[indice_maior_acidente]} acidente(s). ''')

print(f'A média de veiculos nas 5 cidades é {media_veiculos:.0f} veiculos.')

print(f'A media de acidentes nas cidades com mais de 2000 carros é: {media_dos_acidentes:.0f} acidentes.')
