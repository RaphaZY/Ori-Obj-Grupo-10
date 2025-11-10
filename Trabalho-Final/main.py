from model.biblioteca import Biblioteca

def exibir_sobre():
    print("\n==============================")
    print("💻 SISTEMA DE BIBLIOTECA - GRUPO XYZ")
    print("Empresa fictícia: TecBooks Solutions Ltda")
    print("Desenvolvedores: João, Maria e Carlos")
    print("==============================\n")

def menu_cliente(biblioteca, usuario):
    while True:
        print(f"\n👤 Bem-vindo(a), {usuario.get_nome()}!")
        print("1 - Visualizar Empréstimos")
        print("2 - Visualizar Livros")
        print("3 - Sobre")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            biblioteca.listar_emprestimos_cliente(usuario.get_id())
            while True:
                print("\n1 - Fazer um Empréstimo")
                print("2 - Voltar ao Menu Principal")

                opcao = input("Escolha uma opção: ")
                if opcao == "1":
                    if biblioteca.contar_emprestimos_cliente(usuario.get_id()) >= 3:
                        print("❌ Limite de 3 empréstimos atingido.")
                        break
                    id_livro = int(input("Informe o Id do livro: "))
                    if not biblioteca.get_livro_por_id(id_livro):
                        print("Livro não encontrado, tente novamente.")
                        continue
                    else:
                        try:
                            sucesso = biblioteca.fazer_emprestimo(usuario.get_id(), biblioteca.get_livro_por_id(id_livro).get_id())
                            if sucesso:
                                break
                        except Exception as e:
                            print(f"❌ Erro ao fazer empréstimo: {e}")

                elif opcao == "2":
                    break
                else:
                    print("Opção inválida, tente novamente.")
        elif opcao == "2":
            biblioteca.listar_livros()
        elif opcao == "3":
            exibir_sobre()
        elif opcao == "4":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_admin(biblioteca, usuario):
    while True:
        print(f"\n👤 Bem-vindo(a), {usuario.get_nome()}!")
        print("1 - Visualizar Empréstimos")
        print("2 - Visualizar Contas")
        print("3 - Visualizar Livros")
        print("4 - Sobre")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            biblioteca.listar_emprestimos()
            while True:
                print("\n1 - Fazer empréstimo para um Cliente")
                print("2 - Remover empréstimo de um Cliente")
                print("3 - Voltar ao Menu Principal")

                opcao = input("Escolha uma opção: ")
                if opcao == "1":

                    id_cliente = int(input("Informe o Id do cliente: "))
                    if not biblioteca.get_cliente_por_id(id_cliente):
                        print("Cliente não encontrado, tente novamente.")
                        continue

                    if biblioteca.contar_emprestimos_cliente(id_cliente) >= 3:
                        print("❌ Limite de 3 empréstimos atingido.")
                        break

                    id_livro = int(input("Informe o Id do livro: "))
                    if not biblioteca.get_livro_por_id(id_livro):
                        print("Livro não encontrado, tente novamente.")
                        continue
                    else:
                        try:
                            sucesso = biblioteca.fazer_emprestimo(id_cliente, id_livro)
                            if sucesso:
                                break
                        except Exception as e:
                            print(f"❌ Erro ao fazer empréstimo: {e}")

                elif opcao == "2":

                    id_emprestimo = int(input("Informe o Id do emprestimo: "))
                    if not biblioteca.get_emprestimo_por_id(id_emprestimo):
                        print("Empréstimo não encontrado, tente novamente.")
                        continue

                    id_cliente = int(input("Informe o Id do cliente: "))
                    if not biblioteca.get_cliente_por_id(id_cliente):
                        print("Cliente não encontrado, tente novamente.")
                        continue
                   
                    else:
                        try:
                            sucesso = biblioteca.remover_emprestimo(biblioteca.get_emprestimo_por_id(id_emprestimo).get_id(), biblioteca.get_cliente_por_id(id_cliente).get_id())
                            if sucesso:
                                break
                        except Exception as e:
                            print(f"❌ Erro ao fazer empréstimo: {e}")

                elif opcao == "3":
                    break
                else:
                    print("Opção inválida, tente novamente.")
        elif opcao == "2":
            biblioteca.listar_contas()
            while True:
                print("\n1 - Adicionar Conta")
                print("2 - Remover Conta")
                print("3 - Voltar ao Menu Principal")

                opcao = input("Escolha uma opção: ")
                if opcao == "1":

                    pass

                elif opcao == "2":

                    pass

                elif opcao == "3":
                    break
                else:
                    print("Opção inválida, tente novamente.")
        elif opcao == "3":
            biblioteca.listar_livros()
            while True:
                print("\n1 - Adicionar Livro")
                print("2 - Remover Livro")
                print("3 - Voltar ao Menu Principal")

                opcao = input("Escolha uma opção: ")
                if opcao == "1":

                    pass

                elif opcao == "2":

                    pass

                elif opcao == "3":
                    break
                else:
                    print("Opção inválida, tente novamente.")
        elif opcao == "4":
            exibir_sobre()
        elif opcao == "5":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")


def main():
    biblioteca = Biblioteca()
    exibir_sobre()

    login = input("Informe seu login: ")
    senha = input("Informe sua senha: ")

    usuario = biblioteca.autenticar_usuario(login, senha)

    if usuario:
        print(f"\n✅ Login realizado com sucesso ({usuario.get_nome()}: {usuario.get_tipo()})")
        if usuario.get_tipo().lower() == "cliente":
            menu_cliente(biblioteca, usuario)
        else:
            menu_admin(biblioteca, usuario)
    else:
        print("\n❌ Usuário ou senha inválidos. Acesso negado.")

if __name__ == "__main__":
    main()
