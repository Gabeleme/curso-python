
import funcoes_calculadora

def menu_calculadora(): 
    while True: 
        print('--calculadora--\n'
              '1- Operações Básicas\n'
              '2- Operações Cientificas\n'
              '3- Operações Estatistica\n'
              '4- sair')
        opcao = int(input('Informe o que deseja realizar: '))
        print('-'*10)
        if opcao == 1:
            funcoes_calculadora.menu_opera_basica()
        elif opcao == 2:
            funcoes_calculadora.menu_opera_cientifica()
        elif opcao == 3:
            funcoes_calculadora.menu_opera_estatistica()
        elif opcao == 4:
            break
        else:
            print('Opção inválida. Tente novamente.')
menu_calculadora()