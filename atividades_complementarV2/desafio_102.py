'''Crie um programa que tenha uma função fatorial()
que receba dois parametros o primeiro que indique o 
numero a calcular e o outro chamado show, que 
sera um valor logico (opcional) indicando se será 
mostrado ou não na tela o processo de calculo fatorial '''

def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.

    Args:
        param n: O número a ser calculado
        param show: (opcional) mostrar ou não a conta

    Returns:
        o valor do fatorial de um número
    """ 

    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(5, show=True))
help(fatorial)