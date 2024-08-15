''' Uma empresa paga R$ 10.00 por hora normal trabalhada e R$ 15.00 por 
hora extra. Receber o total de horas normais e o total de horas extras 
trabalhadas por um empregado no mês. Calcular e exibir o salário dele.
'''

horas_normais = float(input("Me informe as horas trabalhadas: "))
horas_extras = float(input("Me informe as horas Extras trabalhadas: "))
calc_normais = horas_normais * 10
calc_extra = horas_extras * 15
tot = calc_normais + calc_extra
print('-' * 40)
print(f"O salario do funcionario que trabalhou {horas_normais} horas normais é de {calc_normais}")
print(f"O salario do funcionario que trabalhou {horas_extras} horas extras é de {calc_extra}")
print(f'O salario do funcionario no final somando as horas trabalhadas é de {tot}')


