# EXERCICIO
# Crie uma função que duplicam, triplicam e quadruplicam
# o número recebido como parametro


def multiplicador(valor):
    def multiplicar(x): 
        return x * valor
    return multiplicar

multi_por_dois = multiplicador(2)
multi_por_tres = multiplicador(3)
multi_por_quatro = multiplicador(4)

print(multi_por_dois(10))
print(multi_por_tres(10))
print(multi_por_quatro(10))
