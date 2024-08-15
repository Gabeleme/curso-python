''' Crie um programa que leia o nome e o preço
de varios produtos. O programa deverá perguntar se o usuario
vai continuar No final, mostre:

- Qual é o total gasto na compra
- Quantos produtos custam mais de R$1000
- Qual é o nome do produto mais barato

'''

tot = 0
mais_de_mil = 0
menor = 0
prod_mais_barato = ''
contador = 0

while True:
    nome = str(input("Informe o nome do produto: "))
    preco = float(input("Informe o preço do produto: "))
    
    contador +=1
    tot = tot + preco
    if preco > 1000:
        mais_de_mil += 1
    if contador == 1 or preco < menor:
        menor = preco
        prod_mais_barato = nome
    continuar = ' '
    while continuar not in 'SN': 
        continuar =str(input("Deseja coninuar [s]im ou [n]ão: ")).strip().upper()[0]
    if continuar == 'N':
        break
print("-----FIM DO PROGRAMA-----")
print(f"O total gato na compra foi R${tot:.2f}")
print(f"Existem {mais_de_mil} produtos custando mais de R$1000")
print(f"O produto mais barato foi {prod_mais_barato} que custa R$:{menor:.2f}")