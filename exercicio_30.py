'''
30 - O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, 
que já é um sucesso na sua loja de 1,99. 
Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, 
a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:  Preço do pão: R$ 0.18
-       Panificadora Pão de Ontem - Tabela de preços
                           1 - R$ 0.18
                           2 - R$ 0.36
                                ...
                           50 - R$ 9.00
'''

valor_do_pao = float(input('Digite o valor do pão: '))


contador = 50
print('PANIFICADORA PÃO DE ONTEM'.center(60))
print('=' * 60)
print('Tabela de preço'.center(60))
print('=' * 60)
print('Qnt - Valor'.center(60))
print("")
for i in range(contador +1): 
  print(f' {i} - {valor_do_pao * i:.2f}'.center(60))


print('')
digite_numero = int(input('Digite quantos pães está comprando: '))


total = valor_do_pao * digite_numero
print(f'O consumidor esta comprando {digite_numero} produto(s) e o valor a pagar é R$ {total:.2f} ')