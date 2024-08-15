''' Faça um programa que leia nome e peso de varias pessoas
guardando tudo em uma lista. No final mostre: 

- Quantas pessoas foram cadastradas
- Uma listagem com as pessoas mais pesadas
- Uma listagem com as pessoas mais leves 

Pergunte sempre se quer continuar ou parar 
'''

pessoas = list()
dados = list()
contador = 0
mais_pesada = 0
menos_pesada = 0 

while True:
    dados.append(str(input("Informe seu nome: ")))
    dados.append(float(input("Informe seu peso: ")))
    contador+=1

    pessoas.append(dados[:])
    dados.clear()

    if contador == 1:
         mais_pesada = menos_pesada = pessoas[0][1]
    else:
        if pessoas[-1][1] > mais_pesada:
             mais_pesada = pessoas[-1][1]
        if pessoas[-1][1] < menos_pesada:
            menos_pesada = pessoas[-1][1]


    parar = str(input("deseja continuar [S]im ou [N]ão: ")).strip().upper()[0]
    if parar == 'N':
        break

print('-' * 30)
print(f'Foram Cadastrados {contador} pessoas')
print(f'O maior peso cadastrado foi: {mais_pesada}')
print(f'O menor peso cadastrado foi: {menos_pesada}')