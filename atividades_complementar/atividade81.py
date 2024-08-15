''' Crie um programa que vai ler vários números e colocar em uma lista
Depois disso, mostre: 

- Quantos números foram digitados
- A lista de valores ordenados de forma decrescente
- Se o valor 5 foi digitado e está ou não na lista
'''

listanum = []
p = 'S'
while True:
    listanum.append(int(input(f'Digite um valor: ')))
    p = str(input("deseja continuar [S]im ou [N]ão: ")).strip().upper()[0]
    if p == 'N':
        break

print('-' * 20)
print(f'A quantidade de números digitadas foi: {len(listanum)}')
listanum.sort(reverse=True)
print(f'A lista de valores em forma decrescente é: {listanum}')
if 5 in listanum:
    print("O valor 5 está na lista")
else:
    print("O valor 5 não está na lista")