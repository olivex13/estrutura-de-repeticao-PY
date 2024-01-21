'''
31 - O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 
agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. 
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
Um valor zero deve ser informado pelo operador para indicar o final da compra. 
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, 
para então calcular e mostrar o valor do troco. 
Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. 
A saída deve ser conforme o exemplo abaixo:

-                  Lojas Tabajara 
      Produto 1: R$ 2.20
      Produto 2: R$ 5.80
      Produto 3: R$ 0
      Total: R$ 9.00
      Dinheiro: R$ 20.00
      Troco: R$ 11.00
            ...
'''

print('LOJAS TABAJARA'.center(60))
print('=' * 60)

produtos = []
valores = []

while True:
    produto = input('Digite o produto que está comprando ou sair para ir para pagamento: ').lower()
    if produto == 'sair':
        break
    try:
        valor_produto = float(input("Digite o valor do produto: "))
    except ValueError:
        print("Por favor, digite um valor numérico válido.")
        continue

    produtos.append(produto)
    valores.append(valor_produto)

if len(produtos) == len(valores):
  
    for i in range(len(produtos)):
        print(f"{produtos[i]} - {valores[i]}")
else:
    print("As listas não têm o mesmo comprimento.")

total_da_compra = sum((valores))
recebido = float(input('Digite Quanto de dinheiro recebeu R$: '))

troco = recebido - total_da_compra

main = (f'''O Total da compra é R$ {total_da_compra:.2f}
            O valor recebido foi R$ {recebido:.2f}
            Troco R$ {troco:.2f}        
        ''')

print(main)

