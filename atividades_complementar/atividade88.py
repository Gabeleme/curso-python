''' Faça um programa que ajude um jogador da mega sena
a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo cadastrando em uma lista composta'''

import random

# Pergunta quantos jogos o usuário quer gerar
num_jogos = int(input("Quantos jogos você quer gerar? "))

# Lista para armazenar os palpites
palpites = []

# Gera os jogos
for _ in range(num_jogos):
    # Gera um único jogo com 6 números únicos entre 1 e 60
    jogo = sorted(random.sample(range(1, 61), 6))
    palpites.append(jogo)

# Exibe os palpites gerados
print("\nPalpites gerados:")
for i, palpite in enumerate(palpites, 1):
    print(f"Jogo {i}: {palpite}")
