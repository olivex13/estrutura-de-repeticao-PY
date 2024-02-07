'''Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
          
                         1       0
                         3       10
                         6       15
                         9       20
                         12      25
      mExemplo de saída do programa:

Valor da Dívida	Valor dos Juros	Quantidade de Parcelas	Valor da Parcela
R$ 1.000,00	0	1	R$ 1.000,00
R$ 1.100,00	R$ 100	3	R$ 366,00
R$ 1.150,00	R$ 150	6	R$ 191,67
'''

print('Calculadora de Juros'.center(120))
print('-'*120)

valor = float(input('Digite o valor da dívida: '))
                    
def juros(valor):
   print('Valor da Dívida |	Valor dos Juros	| Quantidade de Parcelas | Valor da Parcela')
   print('-'*120)
   valor_de_juros = {1: 0, 3: 0.1, 6: 0.15, 9: 0.2, 12: 0.25}
   for parcelas, juros in valor_de_juros.items():
    valor_com_juros = valor * (1 + juros)
    valor_parcela = valor_com_juros / parcelas
    print(f"R$ {valor_com_juros:.2f} {' ' * (15 - len(str(valor_com_juros))):<15} {juros * 100:.1f}% {' ' * (17 - len(str(juros * 100))):<17} {parcelas} {' ' * (24 - len(str(parcelas)))} R$ {valor_parcela:.2f}")

juros(valor)

