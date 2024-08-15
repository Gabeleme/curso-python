'''
Crie uma função que fala se um número é par ou impar e retorne
se ele é par ou impar
'''
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} É PAR'
    return f'{numero} É IMPAR'

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

