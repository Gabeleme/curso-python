'''Crie um programa onde o usuario possa digitar sete valores númericos 
e cadastre-os em uma lista única que mantenha separados os valores pares
e impares. No final mostre os valores pares e impares em ordem crescente 
'''

valores = [[], []]

for i in range(7):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    if valor % 2 == 0:
        valores[0].append(valor)  # Adiciona na lista de pares
    else:
        valores[1].append(valor)  # Adiciona na lista de ímpares

# Ordenando os valores
valores[0].sort()  # Ordena a lista de pares
valores[1].sort()  # Ordena a lista de ímpares

# Exibindo os valores pares e ímpares em ordem crescente
print('-' * 30)
print(f"Valores pares em ordem crescente: {valores[0]}")
print(f"Valores ímpares em ordem crescente: {valores[1]}")
