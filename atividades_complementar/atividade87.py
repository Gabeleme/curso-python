''' Aprimore o ex anterior, mostrando no final: 

- a soma de todos os valores pares digitados
- a soma dos valores da terceira coluna
- o maior valor da segunda linha

'''
# Inicializando uma matriz 3x3 com valores vazios
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Preenchendo a matriz com valores lidos pelo teclado
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite um valor para a posição [{i}][{j}]: "))

# Exibindo a matriz formatada
print('-' * 20)
for linha in matriz:
    for valor in linha:
        print(f"[{valor:^5}]", end=" ")
    print()
print('-' * 20)

# soma dos valores pares
soma_par = 0
for linha in matriz:
    for valor in linha:
        if valor % 2 == 0: 
            soma_par += valor

# soma da terceira coluna
soma_terceira_coluna = 0
for i in range(3):
    soma_terceira_coluna += matriz[i][2]

# soma da segunda linha
maior_segunda_linha = max(matriz[1])

print(f'A soma de todos os valores pares digitados é: {soma_par}')
print(f'A soma dos valores inseridos na terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor inserido na segunda linha foi: {maior_segunda_linha}')