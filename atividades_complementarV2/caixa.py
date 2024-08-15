cpf = '123.456.789-00'
senha = '01020304'
saldo = 1000.0

def exibir_menu():
    print('Menu:\n'
          '1 - Saldo\n'
          '2 - Depósito\n'
          '3 - Saque\n'
          '0 - Sair')

def verificar_cpf(cpf_valido):
    while True:
        inserir_cpf = input("Informe seu CPF contendo os traços e pontos: ")
        if inserir_cpf == cpf_valido:
            break
        print("CPF inválido, tente novamente.")

def verificar_senha(senha_valida):
    while True:
        inserir_senha = input("Senha: ")
        if inserir_senha == senha_valida:
            break
        print("Senha incorreta, tente novamente.")

def exibir_saldo(saldo_atual):
    print(f'O saldo total da conta é de R$ {saldo_atual:.2f}')
    print('-' * 30)

def realizar_deposito(saldo_atual):
    while True:
        try:
            deposito = float(input("Informe o valor que deseja depositar: R$ "))
            if deposito < 0:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido. Tente novamente.")
    saldo_atual += deposito
    print(f'Depósito de R$ {deposito:.2f} realizado com sucesso.')
    print(f'O saldo atual é de R$ {saldo_atual:.2f}')
    print('-' * 30)
    return saldo_atual

def realizar_saque(saldo_atual):
    while True:
        try:
            saque = float(input("Informe o valor do saque: R$ "))
            if saque < 0 or saque > saldo_atual:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido ou saldo insuficiente. Tente novamente.")
    saldo_atual -= saque
    print(f'Saque de R$ {saque:.2f} realizado com sucesso.')
    print(f'O saldo atual é de R$ {saldo_atual:.2f}')
    print('-' * 30)
    return saldo_atual

print("--Bem vindo--")
verificar_cpf(cpf)
verificar_senha(senha)
print('-' * 30)

while True:
    exibir_menu()
    try:
        escolha = int(input("Escolha o que deseja realizar: "))
    except ValueError:
        escolha = -1

    if escolha == 0:
        break
    elif escolha == 1:
        exibir_saldo(saldo)
    elif escolha == 2:
        saldo = realizar_deposito(saldo)
    elif escolha == 3:
        saldo = realizar_saque(saldo)
    else:
        print("Valor inválido, escolha novamente.")
        print('-' * 30)

print("Fim do programa")
