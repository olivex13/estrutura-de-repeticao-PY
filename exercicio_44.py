"""44 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

 1 , 2, 3, 4  - Votos para os respectivos candidatos 
 (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
  5 - Voto Nulo
  6 - Voto em Branco
Faça um programa que calcule e mostre:

O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero. """

print("Eleição presidencial".center(120))
print("-" * 120)

print("Candidatos".center(120))
tabelaCandidatos = "1 - Bolsonaro\n2 - Lula\n3 - Ciro\n4 - Simone\n5 - Voto Nulo\n6 - Voto em Branco"
print(tabelaCandidatos)

print("-" * 120)

bolsonaro = 0
lula = 0
ciro = 0
simone = 0
nulo = 0
branco = 0
totalVotos = 0

while True:

    voto = int(input("Digite o número do seu candidato ou 0 para sair: "))

    if voto == 1:
        bolsonaro += 1
        totalVotos += 1
    elif voto == 2:
        lula += 1
        totalVotos += 1
    elif voto == 3:
        ciro += 1
        totalVotos += 1
    elif voto == 4:
        simone += 1
        totalVotos += 1
    elif voto == 5:
        nulo += 1
        totalVotos += 1
    elif voto == 6:
        branco += 1
        totalVotos += 1
    elif voto == 0:
       break
    else:
       print("Digite numero válido")

def calculoNulo (totalVotos, nulo):
  porcentagemNulo = (nulo * 100) / totalVotos
  return porcentagemNulo

def calculoBranco (totalVotos, branco):
  porcentagemBranco = (branco * 100) / totalVotos
  return porcentagemBranco

def vencedor (bolsonaro, lula, ciro, simone):
  if bolsonaro > lula and bolsonaro > ciro and bolsonaro > simone:
    return "Bolsonaro"
  elif lula > bolsonaro and lula > ciro and lula > simone:
    return "Lula"
  elif ciro > bolsonaro and ciro > lula and ciro > simone:
    return "Ciro"
  elif simone > bolsonaro and simone > lula and simone > ciro:
    return "Simone"

porcentagemNulo = calculoNulo(totalVotos, nulo)
procentagemBranco = calculoBranco(totalVotos, branco)
ganhador = vencedor(bolsonaro, lula, ciro, simone)

print("")
print(f'A eleição teve {totalVotos} votos \n \n Bolsonaro teve {bolsonaro} votos \n Lula teve {lula} votos \n Ciro teve {ciro} votos \n Simone teve {simone} votos ')
print("")
print(f'A porcentagem de votos nulos sobre o total de votos foi de {porcentagemNulo} %')
print(f'A porcentagem de votos em branco sobre o total de votos foi de {procentagemBranco} %')
print("")
print(f'O vencedor da eleição foi {ganhador} \n')