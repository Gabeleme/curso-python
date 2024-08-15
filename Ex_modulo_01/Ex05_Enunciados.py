#--------------------------------------------------------------------------------------------
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#--------------------------------------------------------------------------------------------

entrada = input ("Digite um número inteiro: ") #entrada do valor

try: #tratamento de erro / tente executar o código
    entrada_int = int(entrada) # Converte a entrada para um número inteiro e armazena em 'entrada_int'
    par_impar = entrada_int % 2 == 0 # Verifica se o número é par
    par_impar_texto = 'ímpar' # inicializa a variavel chamando impar

    if par_impar: # se par_impar for true (ou seja se ele for PAR)
        par_impar_texto = 'par' # Atualiza 'par_impar_texto' para 'par'

    print(f'O número {entrada_int} é {par_impar_texto}') # Exibe uma mensagem indicando se o número é par ou ímpar
except: # ocorreu algum erro exiba a mensagem 
    print('Você não digitou um número inteiro')

""" F
Se par_impar for verdadeiro e rodar o if, a variavel será alterada para par e seá exibida na tela
caso o if seja falso e não rode a variavel vai continuar com seu valor inicial que é impar e vai ser exibida na tela
e caso ocorra algum erro e a entrada não puder ser convertida para inteiro ela exibe a mensagem de erro

"""