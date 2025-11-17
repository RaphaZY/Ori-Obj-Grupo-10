from model.biblioteca import Biblioteca


# ================
#   Sobre Menu
# ================
def exibir_sobre_menu():
    print("\n==============================")
    print("DLM - Digital Loan Manager")
    print("Empresa Desenvolvedora: Shiny Code")
    print("Empresa Contratante: Biblioteca Municipal Estrela Alpha")
    print("==============================")


# ================
#  Sobre Completo
# ================
def exibir_sobre():
  
    contratante = {
        'nome': 'Biblioteca Municipal Estrela Alpha',
        'slogan': '"Conhecimento que ilumina"',
        'historia': 'Fundada em 1985, a Biblioteca Municipal Estrela Alpha é um dos principais centros culturais da região, atendendo mais de 50.000 usuários anualmente com um acervo de mais de 100.000 volumes.',
        'missao': 'Promover o acesso democrático à informação, fomentar a leitura e ser um espaço de convivência e aprendizado contínuo para a comunidade.'
    }
    
  
    desenvolvedora = {
        'nome': 'Shiny Code',
        'slogan': '"Tecnologia que valoriza saber"',
        'historia': 'Fundada em 2018 por ex-alunos de ciência da computação, a Shiny Code surgiu com o propósito de desenvolver soluções tecnológicas para instituições educacionais e culturais. Em 6 anos, já atendeu mais de 50 clientes no setor público e privado.',
        'valores': [
            'Inovação com propósito',
            'Transparência nas relações',
            'Qualidade técnica acima de tudo',
            'Compromisso com prazos',
            'Aprendizado contínuo',
            'Ética e responsabilidade social'
        ],
        'descricao_logo': 'Hexágono inclinado com gradiente cobre-dourado, lâmpada com filamentos em circuito impresso',
        'paleta_cores': 'Dourado, cobre e cinza-escuro',
        'estilo_fonte': 'Moderna sem serifa com leve arredondamento'
    }
    
   
    sistema = {
        'nome': 'DLM - Digital Loan Manager',
        'slogan': '"Renovações simples. Multas justas. Leitura contínua."',
        'funcionalidades': [
            'Controle digital de empréstimos e devoluções',
            'Sistema de reservas online',
            'Renovação remota',
            'Relatórios gerenciais',
            'Integração com catálogo digital'
        ]
    }
    

    equipe = [
        {
            'nome': 'Gabriel Maximus Rinco Fonseca Rocha',
            'cargo': 'CTO & Lead Developer',
            'responsabilidades': 'Visão tecnológica, arquitetura de sistemas e liderança técnica',
            'expertise': '10+ anos em desenvolvimento de software'
        },
        {
            'nome': 'Gabriel Simões de Oliveira',
            'cargo': 'Product Manager',
            'responsabilidades': 'Coordenação de roadmap, priorização de features e ponte entre clientes e equipe',
            'expertise': 'Gestão ágil e experiência do usuário'
        },
        {
            'nome': 'Matheus Lourenço Buratti',
            'cargo': 'Backend Developer',
            'responsabilidades': 'Desenvolvimento de APIs, integrações, segurança e testes automatizados',
            'expertise': 'Python, Django, APIs REST'
        },
        {
            'nome': 'Raphael Venâncio Coelho',
            'cargo': 'Frontend Developer / UX Engineer',
            'responsabilidades': 'Implementação de interfaces acessíveis, responsivas e centradas no usuário',
            'expertise': 'React, TypeScript, Design System'
        },
        {
            'nome': 'Samuel de Mendonça',
            'cargo': 'QA Engineer / Testador',
            'responsabilidades': 'Estratégias de teste manuais/automatizados e manutenção de pipelines de CI/CD',
            'expertise': 'Testes automatizados, Selenium, Jest'
        },
        {
            'nome': 'Stephen Richard Silva Gomes Lopes Sousa',
            'cargo': 'DevOps / Cloud Engineer',
            'responsabilidades': 'Infraestrutura em nuvem, automação de deploys e observabilidade',
            'expertise': 'AWS, Docker, Kubernetes, Terraform'
        },
        {
            'nome': 'Vinicius do Carmo Soares Barbosa',
            'cargo': 'Analista de Sistemas / Business Analyst',
            'responsabilidades': 'Levantamento de requisitos, modelagem de processos e especificações técnicas',
            'expertise': 'BPMN, UML, Documentação técnica'
        }
    ]

    print("=" * 70)
    print("🎯 PROJETO DLM - BIBLIOTECA MUNICIPAL ESTRELA ALPHA")
    print("=" * 70)
    
    print(f"\n📚 CLIENTE:")
    print(f"   🏛️  {contratante['nome']}")
    print(f"   💡 {contratante['slogan']}")
    print(f"\n   📖 História:")
    print(f"      {contratante['historia']}")
    print(f"\n   🎯 Missão:")
    print(f"      {contratante['missao']}")
    
    print(f"\n💻 DESENVOLVEDORA:")
    print(f"   ✨ {desenvolvedora['nome']} - {desenvolvedora['slogan']}")
    print(f"\n   🏢 História da Shiny Code:")
    print(f"      {desenvolvedora['historia']}")
    print(f"\n   🌟 Valores:")
    for valor in desenvolvedora['valores']:
        print(f"      • {valor}")
    print(f"\n   🎨 Identidade Visual:")
    print(f"      Logo: {desenvolvedora['descricao_logo']}")
    print(f"      Cores: {desenvolvedora['paleta_cores']}")
    print(f"      Fonte: {desenvolvedora['estilo_fonte']}")
    
    print(f"\n🖥️  SISTEMA:")
    print(f"   🔷 {sistema['nome']}")
    print(f"   💬 {sistema['slogan']}")
    print(f"\n   🚀 Funcionalidades Principais:")
    for func in sistema['funcionalidades']:
        print(f"      ✓ {func}")
    
    print(f"\n👥 EQUIPE DE DESENVOLVIMENTO:")
    for membro in equipe:
        print(f"\n   👤 {membro['nome']}")
        print(f"   📋 {membro['cargo']}")
        print(f"   🎯 {membro['responsabilidades']}")
        print(f"   💼 Expertise: {membro['expertise']}")


    print("\n" + "=" * 60)
    print("STATUS: Em desenvolvimento | VERSÃO: 1.0.1")
    print("=" * 60)


# ================
#   Menu Cliente
# ================
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


# ================
#   Menu Admin
# ================
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

                    nome = input("Informe o nome: ")
                    tipo = input("Informe o tipo: ")
                    login = input("Informe o login: ")
                    senha = input("Informe a senha: ")

                    try:
                        sucesso = biblioteca.criar_usuario(nome, tipo, login, senha)
                        if sucesso:
                            break
                    except Exception as e:
                        print(f"❌ Erro ao criar usuário: {e}")

                elif opcao == "2":

                    id_cliente = int(input("Informe o Id do cliente: "))
                    if not biblioteca.get_cliente_por_id(id_cliente):
                        print("Cliente não encontrado, tente novamente.")
                        continue
                    else:
                        try:
                            sucesso = biblioteca.deletar_usuario(id_cliente)
                            if sucesso:
                                break
                        except Exception as e:
                            print(f"❌ Erro ao deletar usuário: {e}")

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

                    nome = input("Informe o nome: ")
                    autor = input("Informe o autor: ")

                    try:
                        sucesso = biblioteca.criar_livro(nome, autor)
                        if sucesso:
                            break
                    except Exception as e:
                        print(f"❌ Erro ao criar usuário: {e}")

                elif opcao == "2":

                    id_livro = int(input("Informe o Id do Livro: "))
                    if not biblioteca.get_livro_por_id(id_livro):
                        print("Livro não encontrado, tente novamente.")
                        continue
                    else:
                        try:
                            sucesso = biblioteca.deletar_livro(id_livro)
                            if sucesso:
                                break
                        except Exception as e:
                            print(f"❌ Erro ao deletar livro: {e}")

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


# ================
#   Main
# ================
def main():
    biblioteca = Biblioteca()
    exibir_sobre_menu()
    while True:
        print("\n1 - Autenticar")
        print("2 - Cadastrar")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            login = input("Informe seu login: ")
            senha = input("Informe sua senha: ")

            usuario = biblioteca.autenticar_usuario(login, senha)

            if usuario:
                print(f"\n✅ Login realizado com sucesso ({usuario.get_nome()}: {usuario.get_tipo()})✅")
                if usuario.get_tipo().lower() == "cliente":
                    menu_cliente(biblioteca, usuario)
                else:
                    menu_admin(biblioteca, usuario)
            else:
                print("\n❌  Acesso negado: Usuário ou senha inválidos ❌")

        elif opcao == "2":
            #autenticação
            pass

        elif opcao == "3":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
