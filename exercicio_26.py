'''

26 - Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''

print('ELEIÇÕES DO PYTHON'.center(60))
print('')

contador = int(input('Digite a quantidade de eleitores: '))
votos = []


for i in range(contador):
    voto = str(input('''Em qual eleitor deseja votar: 
                         [A] João
                         [B] Jose
                         [C] Jonas:
                            =>''')).lower()
    if voto in ['a', 'b', 'c']:
        votos.append(voto)
    else:
        print("Opção inválida. Por favor, escolha A, B ou C.")

contagem_votos = {'a':0, 'b':0, 'c':0}

for voto in votos:
    contagem_votos[voto] += 1

vencedor = max(contagem_votos, key=contagem_votos.get)

print("Resultado da votação:")
for candidato, votos_obtidos in contagem_votos.items():
    print(f"{candidato}: {votos_obtidos} votos")

print(f"\nO vencedor é o candidato {vencedor.upper()} com {contagem_votos[vencedor]} votos.")




    
