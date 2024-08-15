''' Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos preçosna sequencia 

No final mostre uma listagem de preços, organizando os dados
em forma tabular

'''

item = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 
        'Estojo', 25.00, 'Transferidor', 4.20,
        'Compasso', 9.99, 'mochila', 120.00, 'Caneta', 22.30,
        'Livros', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS"}')
print('-' * 40)
for pos in range(0, len(item)):
    if pos % 2 == 0:
        print(f'{item[pos]:.<30}', end='')
    else:
        print(f'R$:{item[pos]:>7.2f}')
print('-' * 40)