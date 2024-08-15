#--------------------------------------------------------------------------------------------
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
#--------------------------------------------------------------------------------------------

primeiro_nome = input("Informe seu primeiro nome: ") #pede para informar o nome

tamanho_nome = len(primeiro_nome) #faz a contagem do nome

if tamanho_nome > 1: #se tamanho nome for maior que 1
    if tamanho_nome <= 4: # e se tamanho nome for menor ou igual a 4
        print('Seu nome é curto') #exibe a mensagem 
    elif tamanho_nome >= 5 and tamanho_nome <= 6: #se tamanho nome for maior ou igual a 5 e menor ou igual a 6
        print('Seu nome é normal') #retorna isso
    else: #se não
        print('Seu nome é muito grande') #retorne isso
else: 
    print('Digite mais de uma letra.')

# observe que existe if e ilif dentro do if e que o primeiro else é os de dentro e o outro do primeiro printipal 