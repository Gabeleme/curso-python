''' Crie um programa que çeia o nome de uma cidade 
e diga se ela começa ou não com o nome Santo '''
cidade = str(input('Digite o nome da sua cidade: ')).strip() #tirando espaço
print(cidade[0:5].upper() == 'SANTO') #joga tudo pra maiusculo e testa

''' colocar para ele jogar tudo pra maiusculo pra testar
evita aquele erro dele escrever ou minuscuo ou maiusculo ou 
mesclado as letras e dar erro'''