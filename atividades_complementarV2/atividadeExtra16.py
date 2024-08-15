
minutos_gastos = float(input('Quantos minutos foram utilizados do seu plano: '))

custo_plano = 50.00
if minutos_gastos <= 50:
    total = custo_plano
else:
    minutos_excedentes = minutos_gastos - 50
    custo_extra = minutos_excedentes * 1.50
    total = custo_plano + custo_extra
print(f'O valor total do seu plano é de R$ {total:.2f}') 