''' Faça um programa que tenha uma função chamada escreva()
que receba um texto qualquer como parametro e mostre uma 
mensagem com tamanho adaptavel '''

def escreva (msg): 
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)

escreva("Gabriela Oliveira")
escreva("Estou fazendo um teste")