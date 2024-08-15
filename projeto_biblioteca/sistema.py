import datetime

livros = [] 
usuarios = [] 
emprestimos = [] 


def cadastro_de_livro(): 
    titulo = input('Título: ')
    autor = input('Autor: ')
    ano_de_publicacao = input('Ano de publicação: ')
    genero = input('Gênero: ')
    isbn = input('ISBN: ')
    quant_de_copias = int(input('Quantidade de cópias disponíveis: '))

    for livro in livros:
        if livro['ISBN'] == isbn:
            print('O livro com esse ISBN já está cadastrado.')
            return 
    
    livro = {
        'Título': titulo,
        'Autor': autor,
        'Ano': ano_de_publicacao,
        'Gênero': genero,
        'ISBN': isbn,
        'Cópias': quant_de_copias
    }
    livros.append(livro)
    print('Livro cadastrado com sucesso!')

def cadastro_usuario():
    nome = input('Nome: ')
    user_id = input('ID: ')
    email = input('E-mail: ')
    telefone = input('Telefone: ')

    for usuario in usuarios:
        if usuario['ID'] == user_id:
            print('Já existe um usuário com esse ID cadastrado.')
            return
    
    usuario = {
        'Nome': nome,
        'ID': user_id,
        'E-mail': email,
        'Telefone': telefone
    }
    usuarios.append(usuario)
    print('Cadastro de usuário realizado com sucesso!')

def emprestimo_livro(): 
    user_id = input("ID do usuário: ")
    isbn = input("ISBN do livro: ")

    usuario = None
    for u in usuarios:
        if u['ID'] == user_id:
            usuario = u
            break
    if not usuario:
        print('Usuário não encontrado.')
        return
    
    livro_encontrado = None
    for l in livros:
        if l['ISBN'] == isbn:
            livro_encontrado = l
            break
    if not livro_encontrado:
        print('Livro não encontrado.')
        return
    if livro_encontrado['Cópias'] <= 0: 
        print('Não há cópias disponíveis deste livro.')
        return
            
    data_emprestimo = datetime.date.today()
    data_devolucao = data_emprestimo + datetime.timedelta(days=14)

    emprestimo = {
        'ID Usuário': user_id,
        'ISBN': isbn,
        'Data de Empréstimo': data_emprestimo,
        'Data de Devolução Prevista': data_devolucao
    }
    emprestimos.append(emprestimo)
    
    livro_encontrado['Cópias'] -= 1  
    print("Empréstimo realizado com sucesso!")

def devolver_livro():
    user_id = input("ID do usuário: ")
    isbn = input("ISBN do livro: ")

    emprestimo_encontrado = None
    for emprestimo in emprestimos:
        if emprestimo['ID Usuário'] == user_id and emprestimo['ISBN'] == isbn:
            emprestimo_encontrado = emprestimo
            break

    if not emprestimo_encontrado:
        print("Empréstimo não encontrado.")
        return

    for livro in livros:
        if livro['ISBN'] == isbn:
            livro['Cópias'] += 1
            break

    data_devolucao_real = datetime.date.today()
    emprestimos.remove(emprestimo_encontrado)
    print("Livro devolvido com sucesso!")

def exibir_menu():
    while True: 
        print('--Bem-Vindo à Biblioteca--\n'
              '1 - Cadastrar livro\n'
              '2 - Cadastrar usuário\n'
              '3 - Realizar empréstimo\n'
              '4 - Devolver livro\n'
              '5 - Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastro_de_livro()
        elif opcao == '2':
            cadastro_usuario()
        elif opcao == '3':
            emprestimo_livro()
        elif opcao == '4':
            devolver_livro()
        elif opcao == '5':
            break
        else:
            print('Opção inválida. Tente novamente.')

exibir_menu()




        






