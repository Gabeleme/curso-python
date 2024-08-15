''' Faça um programa que jogue par ou impar com o computador
O jogo so será interrompido quando o jogador PERDER
mostrando o total de vitorias consecutivas que ele 
conquistou no final do jogo'''

import random

# Inicializando variáveis
vitorias = 0

print("Vamos jogar Par ou Ímpar!")
while True:
    # Entrada do usuário
    escolha_usuario = ''
    while escolha_usuario not in ['P', 'I']:
        escolha_usuario = input("Escolha Par (P) ou Ímpar (I): ").strip().upper()
    
    numero_usuario = int(input("Digite um número: "))
    
    # Escolha do computador
    numero_computador = random.randint(0, 10)
    total = numero_usuario + numero_computador
    resultado = 'P' if total % 2 == 0 else 'I'
    
    # Exibindo escolhas
    print(f"Você escolheu {numero_usuario} e o computador escolheu {numero_computador}. Total: {total} - {'Par' if resultado == 'P' else 'Ímpar'}")
    
    # Verificando quem ganhou
    if resultado == escolha_usuario:
        print("Você ganhou!")
        vitorias += 1
    else:
        print("Você perdeu!")
        break

# Exibindo total de vitórias
print(f"Total de vitórias consecutivas: {vitorias}")

