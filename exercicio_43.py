'''
43 - O cardápio de uma lanchonete é o seguinte:
| Especificação    | Código | Preço   |
|-------------------|--------|---------|
| Cachorro Quente  | 100    | R$ 1,20 |
| Bauru Simples    | 101    | R$ 1,30 |
| Bauru com ovo    | 102    | R$ 1,50 |
| Hambúrguer       | 103    | R$ 1,20 |
| Cheeseburguer    | 104    | R$ 1,30 |
| Refrigerante     | 105    | R$ 1,00 |

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.'''

print('Lanchonete do Sr. Python'.center(60))
print('-' * 60)

descricao_pedido = ""

total_geral = 0
menu = ('''     MENU
| Especificação    | Código | Preço   |
|-------------------|--------|---------|
| Cachorro Quente  | 100    | R$ 1,20 |
| Bauru Simples    | 101    | R$ 1,30 |
| Bauru com ovo    | 102    | R$ 1,50 |
| Hambúrguer       | 103    | R$ 1,20 |
| Cheeseburguer    | 104    | R$ 1,30 |
| Refrigerante     | 105    | R$ 1,00 |

        ''')

cardapio = {
     100: {"nome": "Cachorro Quente", "preco": 1.20},
    101: {"nome": "Bauru Simples", "preco": 1.30},
    102: {"nome": "Bauru com ovo", "preco": 1.50},
    103: {"nome": "Hambúrguer", "preco": 1.20},
    104: {"nome": "Cheeseburguer", "preco": 1.30},
    105: {"nome": "Refrigerante", "preco": 1.00}
}

print(menu)
print('')

while True:
    codigo = input('Digite o código do lanche ou 0 para encerrar.')
    codigo = int(codigo)
    if codigo == 0:
        break
    quantidade = input('Digite a quantidade desejada: ')
    quantidade = int(quantidade)

    if codigo in cardapio:
        nome_item = cardapio[codigo]["nome"]
        preco_item = cardapio[codigo]["preco"]
        valor_item = preco_item * quantidade
        total_geral += valor_item
        descricao_pedido += f"{quantidade}x {nome_item}: R$ {valor_item:.2f}\n"
    else:
     print("Código de item inválido. Tente novamente.")

print("")
print("Detalhes do Pedido:")
print(descricao_pedido)
print(f"Total Geral: R$ {total_geral:.2f}")