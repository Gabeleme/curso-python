#----------------------------------------------------
'''
Repetições 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
break -> busca o while mais proximo dele e vai fechar o programa e sair fora do laço 

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')
'''
#----------------------------------------------------

contador = 0

while contador <= 10:
    contador = contador + 1
    print(contador)

print('Acabou')

#----------------------------------------------------

"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""
#----------------------------------------------------

# Uso do continue

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break


print('Acabou')

#----------------------------------------------------
# While dentro de while 

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1


print('Acabou')

#----------------------------------------------------
