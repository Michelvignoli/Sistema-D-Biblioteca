usuarios = []
livros = []

def menu_principal():
    while True:
        try:
            print("\nBem vindo! Escolha uma das opções abaixo:")
            print("1. Login")
            print("2. Gerenciar usuários")
            print("3. Cadastrar livros")
            print("4. Buscar livros")
            print("5. Sair")

            opcao = input("Digite a opção desejada: ")

            if opcao == '1':
                login()
            elif opcao == '2':
                gerenciar_usuarios()
            elif opcao == '3':
                cadastrar_livros(livros)
            elif opcao == '4':
                buscar_livros()
            elif opcao == '5':
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

def login():
    try:
        nome = input("Digite o nome do usuário: ")
        senha = input("Digite a senha: ")
        for usuario in usuarios:
            if usuario['usuario'] == nome and usuario['senha'] == senha:
                print(f"Bem-vindo, {nome}!")
                return
        print("Usuário ou senha incorretos. Tente novamente.")
    except KeyError:
        print("Erro: Dados de usuário incorretos. Verifique o formato.")
    except Exception as e:
        print(f"Erro inesperado durante o login: {e}")

def cadastrar_livros(livros):
    try:
        print("Cadastrar livros")
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o nome do autor do livro: ")
        try:
            ano = int(input("Digite o ano de publicação do livro: "))
            livros.append({'titulo': titulo, 'autor': autor, 'ano': str(ano)})
            print(f"Livro '{titulo}' cadastrado com sucesso!")
        except ValueError:
            print("Erro: O ano deve ser um número inteiro.")
    except Exception as e:
        print(f"Erro inesperado ao cadastrar livro: {e}")

def buscar_livros():
    try:
        print("Buscar livros")
        criterio = input("Você quer buscar por título, autor ou ano? ").lower()
        termo = input(f"Digite o {criterio} que deseja buscar: ")

        if criterio not in ['título', 'autor', 'ano']:
            print("Critério inválido. Use 'título', 'autor' ou 'ano'.")
            return

        resultados = []
        for livro in livros:
            try:
                if criterio == 'título' and termo.lower() in livro['titulo'].lower():
                    resultados.append(livro)
                elif criterio == 'autor' and termo.lower() in livro['autor'].lower():
                    resultados.append(livro)
                elif criterio == 'ano' and termo == livro['ano']:
                    resultados.append(livro)
            except KeyError:
                print(f"Aviso: Um livro não possui o campo '{criterio}'. Ignorando.")

        if resultados:
            print("Livros encontrados:")
            for livro in resultados:
                print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
        else:
            print(f"Nenhum livro encontrado para o {criterio} '{termo}'.")
    except Exception as e:
        print(f"Erro inesperado ao buscar livros: {e}")

def gerenciar_usuarios():
    while True:
        try:
            print("\n-------------------------------")
            print("ESCOLHA A OPÇÃO DESEJADA")
            print("1. Cadastrar usuário")
            print("2. Gerar relatórios de usuários")
            print("3. Gerar relatórios de livros")
            print("4. Voltar ao menu principal")

            opcao = input("Digite a opção desejada: ")

            if opcao == '1':
                cadastrar_usuario()
            elif opcao == '2':
                gerar_relatorios_usuarios()
            elif opcao == '3':
                gerar_relatorios_livros()
            elif opcao == '4':
                break
            else:
                print("Opção inválida, tente novamente.")
        except Exception as e:
            print(f"Erro inesperado no menu de gerenciamento: {e}")

def cadastrar_usuario():
    try:
        nome = input("Digite o nome do usuário: ")
        senha = input("Digite a senha para cadastro: ")
        usuarios.append({'usuario': nome, 'senha': senha})
        print(f"Usuário {nome} com senha {senha} cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro inesperado ao cadastrar usuário: {e}")

def gerar_relatorios_usuarios():
    try:
        if not usuarios:
            print("Não há usuários cadastrados.")
        else:
            print("Segue lista com relatórios de usuários:")
            for usuario in usuarios:
                print(f"Nome: {usuario['usuario']}")
    except KeyError:
        print("Erro: Formato de usuário inválido.")
    except Exception as e:
        print(f"Erro inesperado ao gerar relatório de usuários: {e}")

def gerar_relatorios_livros():
    try:
        if not livros:
            print("Não há livros cadastrados.")
        else:
            print("Lista de livros cadastrados:")
            for livro in livros:
                print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
    except KeyError:
        print("Erro: Formato de livro inválido.")
    except Exception as e:
        print(f"Erro inesperado ao gerar relatório de livros: {e}")

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print(f"Erro crítico: {e}")