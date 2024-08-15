'''Crie um programa que crie uma matriz de dimensão 3x3 
e preencha com valores lidos pelo teclado

No final mostre a matriz na tela, com a formatação correta
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
