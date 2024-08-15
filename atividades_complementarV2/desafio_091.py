''' Crie um programa onde 4 jogadores joguem um dado e tenham 
resultados aleatorios. Guarde esses resultados em um dicionario. 
No final coloqueesse dicionario em ordem sabendo que o vencedor 
tirou o maior numero no dado'''

from random import randint #import gerar números aleatorios
from time import sleep 
from operator import itemgetter # import facilitar a ordenação

#Criação do dicionario 
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()  # Inicializa uma lista vazia
print('Valores sorteados: ') 

for k, v in jogo.items(): # Itera sobre os itens do dicionário 'jogo', onde k é a chave (nome do jogador) e v é o valor (número sorteado)
    print(f'{k} tirou {v} no dado') # Exibe o nome do jogador e o número sorteado
    sleep(1)  # Pausa a execução por 1 segundo 
    
# Ordena os itens do dicionário 'jogo' com base nos valores (números sorteados) em ordem decrescente
# O itemgetter(1) indica que a ordenação deve ser feita com base no segundo elemento de cada tupla (o valor sorteado)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-' * 30)
print('  --Ranking dos Jogadores --')
for i, v in enumerate(ranking): # Itera sobre a lista 'ranking', onde i é o índice (posição do jogador no ranking) e v é o item (tupla com nome do jogador e valor sorteado)
    print(f'   {i+1} lugar: {v[0]} com {v[1]}') # Exibe a posição no ranking, o nome do jogador e o valor sorteado
    sleep(1)  # Pausa a execução por 1 segundo para tornar a saída mais legível