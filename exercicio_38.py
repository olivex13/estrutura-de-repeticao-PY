'''
38 - Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
-  Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
- Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
- A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
- Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''

print('AUMENTO DE SALARIO'.center(60))
print('=' * 60)


ano_contratacao = 1995
salario_inicial = float(input('Digite o salario inicial: R$ '))
percentual_aumento = 1.5

ano_atual = int(input("Digite o ano atual: "))

for ano in range(1997, ano_atual+1):
    percentual_aumento *= 2    
  
    aumento_salarial = salario_inicial * (percentual_aumento / 100)
    
    salario_inicial += aumento_salarial
    
    print(f"Ano {ano}: Salário R$ {salario_inicial:.2f} - Porcentagem de aumento {percentual_aumento} %")

