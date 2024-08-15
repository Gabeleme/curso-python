import math
from collections import Counter

def menu_opera_basica():
    while True:
        print('Operações Básicas\n'
             '1- Soma\n'
             '2- Subtração\n'
             '3- Multiplicação\n'
             '4- Divisão\n'
             '5- Sair')
        
        opcao_basica = int(input('Informe o que deseja realizar: '))
        print('-'*10)

        if opcao_basica == 1:
            num_count = int(input("Quantos números você deseja somar? "))
            soma = 0
            for i in range(num_count):
                num = float(input(f"Digite o número {i + 1}: "))
                soma += num
            print(f"O resultado da soma é: {soma}")
            print('-'*10)
        elif opcao_basica == 2:  
            num_count = int(input("Quantos números você deseja subtrair? "))
            if num_count < 2:
                print("Você precisa de pelo menos dois números para subtrair.")
                continue
            resultado = float(input("Digite o primeiro número: "))
            for i in range(1, num_count):
                num = float(input(f"Digite o número {i + 1}: "))
                resultado -= num
            print(f"O resultado da subtração é: {resultado}")
            print('-'*10)
        elif opcao_basica == 3:
            num_count = int(input("Quantos números você deseja Multiplicar: "))
            if num_count < 2:
                print("Você precisa de pelo menos dois números para Multiplicar.")
                continue
            resultado = float(input('Digite o Primeiro número: '))
            for i in range(1, num_count):
                num = float(input(f"Digite o número {i + 1}: "))
                resultado *= num
            print(f'o resultado da Multiplicação é: {resultado}')
            print('-'*10)
        elif opcao_basica == 4:
            num_count = int(input("Quantos números você deseja dividir? "))
            if num_count < 2:
                print("Você precisa de pelo menos dois números para dividir.")
                continue
            resultado = float(input("Digite o primeiro número: "))
            for i in range(1, num_count):
                num = float(input(f"Digite o número {i + 1}: "))
                if num != 0:
                    resultado /= num
                else:
                    print("Erro: Divisão por zero não é permitida.")
                    resultado = None
                    break
            if resultado is not None:
                print(f"O resultado da divisão é: {resultado}")
                print('-'*10)
            
        elif opcao_basica == 5:
            break
        else:
            print('Opção inválida. Tente novamente.')

def fatoracao(n):
    fatores = []
    divisor = 2 #menor numero primo
    while n > 1: # para quando for menor que 1
        if n % divisor == 0: #verifica se é divisivel
            fatores.append(divisor) #adiciona a lista
            n //= divisor
        else:
            divisor += 1
    return fatores

def menu_opera_cientifica():
    while True:
        print('Operações Cientificas\n'
              '1- Seno\n'
              '2- Cosseno\n'
              '3- Tangente\n'
              '4- Logaritmos\n'
              '5- Fatoração\n'
              '6- Sair')
        opcao_cientifica = int(input('Informe o que deseja realizar: '))
        print('-'*10)
        if opcao_cientifica == 1:
            angulo_graus = float(input('Digite o ângulo em graus: '))
            #conversão para radiano
            angulo_radianos = math.radians(angulo_graus)
            #calculo do seno
            seno = math.sin(angulo_radianos)
            print(f'O seno de {angulo_graus} graus é: {seno}')
            print('-'*10)
        elif opcao_cientifica == 2:
            angulo_graus = float(input('Informe o ângulo em graus: '))
            angulo_radianos = math.radians(angulo_graus)
            cosseno = math.cos(angulo_radianos)
            print(f'O cosseno de {angulo_graus} graus é: {cosseno}')
            print('-'*10)
        elif opcao_cientifica == 3:
            angulo_graus = float(input('Informe o ângulo em graus: '))
            angulo_radianos = math.radians(angulo_graus)
            tangente = math.tan(angulo_radianos)
            print(f'A tangente de {angulo_graus} graus é: {tangente}')
            print('-'*10)
        elif opcao_cientifica == 4:
            valor = float(input('Digite o número para calcular o logaritmo: '))
            print('Bases: \n'
                  '1- Base 10\n'
                  '2- Base e (logaritmo natural)') # com valor de aprox 2,71828
            escolha = int(input("Digite 1 ou 2: "))
            if escolha == 1:
                logaritmo_valor = math.log10(valor)
                print(f"O logaritmo de {valor} na base 10 é {logaritmo_valor}")
            elif escolha == 2:
                logaritmo_valor = math.log(valor)
                print(f'O logaritmo natural de {valor} é {logaritmo_valor}')
            else:
                print("Escolha inválida! Por favor, digite 1 ou 2.")
        elif opcao_cientifica == 5:
            numero = int(input("Digite um número para fatorar: "))
            fatores = fatoracao(numero)
            print(f"Fatores primos de {numero}: {fatores}")
            print('-'*10)
        elif opcao_cientifica == 6:
            break
        else:
            print('Opção inválida. Tente novamente.')

def calcular_media(valores):
    return sum(valores) / len(valores) #sum - soma todos, len - num de elementos na lista

def calcular_mediana(valores):
    valores_ordenados = sorted(valores) #sorted - ordena os elementos
    n = len(valores_ordenados)
    meio = n // 2
    if n % 2 == 0:
        return(valores_ordenados[meio - 1] + valores_ordenados[meio] / 2)
    else:
        return valores_ordenados[meio]

def calcular_moda(valores):
    contagem = Counter(valores)
    maxima_freq = max(contagem.values())
    return [valor for valor, freq in contagem.items() if freq == maxima_freq]

def calcular_variancia(valores):
    media = calcular_media(valores)
    return sum((x - media) ** 2 for x in valores) / len(valores)

def calcular_desvio_padrao(valores):
    variancia = calcular_variancia(valores)
    return math.sqrt(variancia)

def calcular_permutacoes(n, r): #n- elementos r-elementos a serem escolhidos
    return math.perm(n, r)

def calcular_combinacoes(n, r):
    return math.comb(n, r)

def menu_opera_estatistica(): 
    while True:
        print('Operações Estatisticas\n'
              '1- Média\n'
              '2- Moda\n'
              '3- Mediana\n'
              '4- Variância e Desvio Padrão\n'
              '5- Permutações e Combinações\n'
              '6- Sair')
        opcao_estatistica = int(input('Informe o que deseja realizar: '))
        print('-'*10)
        if opcao_estatistica == 1:
           valores = list(map(float, input('Digite os valores separados por espaço: ').split()))
           print("Média:", calcular_media(valores))
        elif opcao_estatistica == 2:
            valores = list(map(float, input('Digite os valores separados por espaço: ').split()))
            print("Moda:", calcular_moda(valores))
        elif opcao_estatistica == 3:
            valores = list(map(float, input('Digite os valores separados por espaço: ').split()))
            print("Mediana:", calcular_mediana(valores))
        elif opcao_estatistica == 4:
            valores = list(map(float, input('Digite os valores separados por espaço: ').split()))
            print("Variância:", calcular_variancia(valores))
            print("Desvio Padrão:", calcular_desvio_padrao(valores))
        elif opcao_estatistica == 5:
            n = int(input('Digite o valor de n: '))
            r = int(input('Digite o valor de r: '))
            print(f"Permutações de {n} objetos tomados {r} de cada vez:", calcular_permutacoes(n, r))
            print(f"Combinações de {n} objetos tomados {r} de cada vez:", calcular_combinacoes(n, r))
        elif opcao_estatistica == 6:
            break
        else:
            print('Opção inválida. Tente novamente.')

def menu_calculadora(): 
    while True: 
        print('--calculadora--\n'
              '1- Operações Básicas\n'
              '2- Operações Cientificas\n'
              '3- Operações Estatistica\n'
              '4- sair')
        opcao = int(input('Informe o que deseja realizar: '))
        print('-'*10)
        if opcao == 1:
            menu_opera_basica()
        elif opcao == 2:
            menu_opera_cientifica()
        elif opcao == 3:
            menu_opera_estatistica()
        elif opcao == 4:
            break
        else:
            print('Opção inválida. Tente novamente.')
menu_calculadora()