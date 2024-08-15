''' Crie um programa que vai ler varios números e colocar em uma lista
Depois disso crie duas listas extras que vão conter apenas os valores pares e 
os valores impares digitados respectivamente

Ao final mostre o conteudo das 3 listas geradas

'''

listanum = []
lista_par = []
lista_impar = []


while True:
    valor = (int(input(f'Digite um valor: ')))
    listanum.append(valor)

    p = str(input("deseja continuar [S]im ou [N]ão: ")).strip().upper()[0]
    if p == 'N':
        break

if valor % 2 == 0:
    lista_par.append(listanum)
else:
    lista_impar.append(listanum)


print(f'O valores digitados foram: {listanum}')
print(f'Os valores digitados par foram: {lista_par}')
print(f'Os valores digitados impar foram: {lista_impar}')
