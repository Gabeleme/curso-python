# -----------------------------------------------------------------------

# Operadores 

adicao = 10 + 10 
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3 #corta as casas decimais 
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

# é divisivel?
print(10 % 8 == 0) 
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)

# -----------------------------------------------------------------------

concatenacao = 'Luiz' + ' ' + 'Otávio'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_luiz = 3 * 'Luiz'
print(a_dez_vezes)
print(tres_vezes_luiz)

# -----------------------------------------------------------------------
#Precedencia dos Operadores

# 1. (n + n) #sempre executao por primeiro e de dentro pra fora
# 2. **
# 3. * / // %
# 4. + -

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)

# -----------------------------------------------------------------------