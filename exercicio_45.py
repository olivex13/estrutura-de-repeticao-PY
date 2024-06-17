'''
45 - Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
- Maior e Menor Acerto;
- Total de Alunos que utilizaram o sistema;
- A Média das Notas da Turma.
Gabarito da Prova:

- 01 - A
- 02 - B
- 03 - C
- 04 - D
- 05 - E
- 06 - E
- 07 - D
- 08 - C
- 09 - B
- 10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
'''


print('SISTEMA PARA VERIFICAR NOTAS'.center(60))
print("=" * 60)

def verificar_respostas():
    print("Professor, insira o gabarito da prova:")
    gabarito = []
    for i in range(10):
        resposta = input(f"Gabarito da questão {i+1}: ").strip().upper()
        gabarito.append(resposta)
    
    alunos_notas = []
    
    while True:
        print("\nDigite as respostas do aluno:")
        respostas_aluno = []
        for i in range(10):
            resposta = input(f"Questão {i+1}: ").strip().upper()
            respostas_aluno.append(resposta)
        
        acertos = sum(1 for i in range(10) if respostas_aluno[i] == gabarito[i])
        alunos_notas.append(acertos)
        
        outro_aluno = input("Outro aluno vai utilizar o sistema? (S/N): ").strip().upper()
        if outro_aluno != 'S':
            break
    
    maior_acerto = max(alunos_notas)
    menor_acerto = min(alunos_notas)
    total_alunos = len(alunos_notas)
    media_notas = sum(alunos_notas) / total_alunos
    
    print("\nResultados da turma:")
    print(f"Maior acerto: {maior_acerto}")
    print(f"Menor acerto: {menor_acerto}")
    print(f"Total de alunos: {total_alunos}")
    print(f"Média das notas: {media_notas:.2f}")

verificar_respostas()
