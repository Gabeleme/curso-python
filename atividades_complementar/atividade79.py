''' Crie um programa onde o usuario possa digitar varios valores 
númericos e cadastre-os em uma lista. Caso o número ja exista la 
dentro ele não será adicionado. No final será exibido todos os
valores unicos digitados em ordem crescente '''

listanum = []
while True:
    valor = int(input('Digite um valor: '))
    
    if valor not in listanum:
        listanum.append(valor)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor já existente! Não será adicionado.")
    
    p = input("Deseja continuar [S]im ou [N]ão: ").strip().upper()
    if p == 'N':
        break

# Ordenando a lista em ordem crescente
listanum.sort()

# Exibindo os valores únicos em ordem crescente
print("Valores únicos digitados em ordem crescente:")
for valor in listanum:
    print(valor, end=' ')
