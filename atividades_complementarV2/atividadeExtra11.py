'''Receber um número e verificar se ele esta na faixa de 0 à 9. Se sim, 
mostre uma mensagem afirmativa, caso contrário mostre uma mensagem 
indicando que o número não se encontra na faixa.'''

valor = int(input("Informe um valor: "))

if 0 <= valor <= 9:
    print(f"O seu número {valor} está entre 0 e 9")
else:
    print(f'O número {valor} informado não está entre 0 e 9')