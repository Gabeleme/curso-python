#--------------------------------------------------------------------------------------------
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
#--------------------------------------------------------------------------------------------

entrada= input("Informe a hora em números inteiros: ") # pede a entrada do valor

try: #tratamento de erros
    hora = int(entrada) # converte a entrada para um valor inteiro e armazena na variavel hora

    if hora >= 0 and hora <=11: # se hora for maior ou igual a zero e hora for menor ou igual a 11
        print("Bom Dia!!") #exibe isso
    elif hora >= 12 and hora <= 17: # se hora for maior ou igual a 12 e menor ou igual a 17
        print("Boa Tarde!!") #exibe isso
    elif hora >= 18 and hora <= 23: # se a hora for maior ou igual a 18 e menor ou igual a 23
        print("Boa noite!") #exibe isso
    else: # se não
        print("Não conheço a hora que foi informada") #exibe isso
except: # ocorreu algum erro exiba a mensagem 
    print("Por favor, digite apenas números inteiros") #exibe isso
