'''Crie um programa que gerencie o aproveitamento de um jogador de futebol
O programa vai ler o nome do jogador e quantas partidas ele jogou
Depois vai ler a quantidade de gols feitos em cada partida
No final, tudo isso será guardado em um dicionario, Incluindo o total
de gols feitos furante o campeonato '''

jogador = dict()
partida = list()
jogador ['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? ')) 
for c in range(0, tot):
    partida.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['gols'] = partida[:]
jogador['total'] = sum(partida)
print('-' * 30)
print(jogador)
print('-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'   -- Na partida {i} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')