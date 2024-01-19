'''
29 - O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
-        Lojas Quase Dois - Tabela de preços
                    1 - R$ 1.99
                    2 - R$ 3.98
                        ...
                    50 - R$ 99.50

'''

VALOR_PRODUTO = 1.99


contador = 50
print('LOJA QUASE DOIS'.center(60))
print('=' * 60)
print('Tabela de preço'.center(60))
print('=' * 60)
print('Qnt - Valor'.center(60))
print("")
for i in range(contador +1): 
  print(f' {i} - {VALOR_PRODUTO * i:.2f}'.center(60))


print('')
digite_numero = int(input('Digite o numero de produtos que está comrando: '))


total = VALOR_PRODUTO * digite_numero
print(f'O consumidor esta comprando {digite_numero} produto(s) e o valor a pagar é R$ {total:.2f} ')