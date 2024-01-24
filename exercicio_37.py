'''
37 - Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, 
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos 
clientes da academia seu código, sua altura e seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, 
do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.
'''

print('Academia do Python'.center(60))
print('='*60)

codigos = []
alturas = []
pesos = []

while True:
    codigo = input('Digite o codigo do cliente ou 0 para sair: ')
    if codigo == '0':
        break
    else:
        codigos.append(int(codigo))
        altura = float(input('Digite a altura do cliente: '))
        alturas.append(altura)
        peso = float(input('Digite o peso do cliente: '))     
        pesos.append(peso)


indice_menor_peso = pesos.index(min(pesos))

indice_maior_peso = pesos.index(max(pesos))

indice_menor_altura = alturas.index(min(alturas))

indice_maior_altura = alturas.index(max(alturas))

def media_pesos(pesos):
    contador = 0
    for peso in pesos:
        contador += 1 
    media = sum(pesos) / contador
    return media

def media_altura(alturas):
    contador = 0
    for altura in alturas:
        contador += 1
    media = sum(alturas) / contador
    return media

media_de_peso = media_pesos(pesos)
media_de_altura = media_altura(alturas)

print('')
print(f'''O cliente de código {codigos[indice_maior_peso]} é o mais pesado com {pesos[indice_maior_peso]:.2f} kg e {alturas[indice_maior_peso]:.2f} metros.
      
      O cliente de código {codigos[indice_menor_peso]} é o mais leve com {pesos[indice_menor_peso]:.2f} kg e {alturas[indice_menor_peso]:.2f} metros.

      O cliente de código {codigos[indice_menor_altura]} é o mais baixo com {alturas[indice_menor_altura]:.2f} metros e {pesos[indice_menor_altura]:.2f} kg.

      O cliente de código {codigos[indice_maior_altura]} é o mais alto com {alturas[indice_maior_altura]:.2f} metros e {pesos[indice_maior_altura]:.2f} kg.

      A media de peso é {media_de_peso:.2f}.

      A media de altura é {media_de_altura:.2f}.
''')
