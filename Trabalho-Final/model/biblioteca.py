import os
from datetime import date, timedelta
from model.usuario import Usuario
from model.livro import Livro
from model.emprestimo import Emprestimo


class Biblioteca:
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.__data_path = os.path.join(base_path, "..", "data")

        # ✅ Encapsulamento
        self.__usuarios = self.__carregar_usuarios()
        self.__livros = self.__carregar_livros()
        self.__emprestimos = self.__carregar_emprestimos()

    # ------------------- GETTERS -------------------
    def get_usuarios(self):
        return self.__usuarios

    def get_livros(self):
        return self.__livros
    
    def get_livro_por_id(self, id_livro):
        for livro in self.__livros:
            if int(livro.get_id()) == int(id_livro):
                return livro

    def get_emprestimos(self):
        return self.__emprestimos
    
    def get_emprestimo_por_id(self, id_emprestimo):
        for emprestimo in self.__emprestimos:
            if int(emprestimo.get_id()) == int(id_emprestimo):
                return emprestimo
    
    def get_cliente_por_id(self, id_cliente):
        for usuario in self.__usuarios:
            if int(usuario.get_id()) == int(id_cliente):
                return usuario

    # ------------------- LOGIN -------------------
    def autenticar_usuario(self, login, senha):
        for usuario in self.__usuarios:
            if usuario.validar_login(login, senha):
                return usuario
        return None

    # ------------------- CARREGAR ARQUIVOS -------------------
    def __carregar_usuarios(self):
        usuarios = []
        caminho = os.path.join(self.__data_path, "usuarios.txt")
        with open(caminho, "r", encoding="utf-8") as f:
            for linha in f:
                id, nome, tipo, login, senha = linha.strip().split(";")
                usuario = Usuario()
                usuario.set_id(id)
                usuario.set_nome(nome)
                usuario.set_tipo(tipo)
                usuario.set_login(login)
                usuario.set_senha(senha)
                usuarios.append(usuario)
        return usuarios

    def __carregar_livros(self):
        livros = []
        caminho = os.path.join(self.__data_path, "livros.txt")
        with open(caminho, "r", encoding="utf-8") as f:
            for linha in f:
                id, titulo, autor = linha.strip().split(";")
                livro = Livro()
                livro.set_id(id)
                livro.set_titulo(titulo)    
                livro.set_autor(autor)
                livros.append(livro)
        return livros

    def __carregar_emprestimos(self):
        emprestimos = []
        caminho = os.path.join(self.__data_path, "emprestimos.txt")

        with open(caminho, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                # Pular linhas vazias ou com poucos campos
                if not linha or len(linha.split(";")) < 5:
                    continue

                id_emp, id_cli, id_liv, data_ini, data_ent = linha.split(";")
                emprestimo = Emprestimo()
                emprestimo.set_id_emprestimo(id_emp)
                emprestimo.set_id_cliente(id_cli)
                emprestimo.set_id_livro(id_liv)
                emprestimo.set_data_inicio(data_ini)
                emprestimo.set_data_entrega(data_ent)
                emprestimos.append(emprestimo)

        return emprestimos


    # ------------------- LISTAGENS -------------------
    def listar_livros(self):
        print("\n📚 Livros disponíveis:")
        for livro in self.get_livros():
            print(f" - {livro}")

    def listar_emprestimos_cliente(self, id_cliente):
        print("\n📄 Empréstimos do usuário:")
        emprestimos_usuario = [e for e in self.get_emprestimos() if int(e.get_id_cliente()) == int(id_cliente)]
        if not emprestimos_usuario:
            print("Nenhum empréstimo encontrado.")
        else:
            for e in emprestimos_usuario:
                print(f" - {e}")

    def listar_emprestimos(self):
        print("\n📄 Todos os empréstimos:")
        for e in self.get_emprestimos():
            print(f" - {e.listar_admin()}")
        
    def listar_contas(self):
        print("\n📄 Todos as contas:")
        for c in self.get_usuarios():
            print(f" - {c}")

    # ------------------- ARQUIVO -------------------
    def __salvar_emprestimos(self):
        caminho = os.path.join(self.__data_path, "emprestimos.txt")
        with open(caminho, "w", encoding="utf-8") as f:
            for e in self.__emprestimos:
                f.write(e.to_string_line())

    # ------------------- CONTAR -------------------
    def contar_emprestimos_cliente(self, id_cliente):
        idc = int(id_cliente)
        return sum(1 for e in self.__emprestimos if int(e.get_id_cliente()) == idc)

    # ------------------- NOVO EMPRÉSTIMO -------------------
    def fazer_emprestimo(self, id_cliente, id_livro):
        
        total = self.contar_emprestimos_cliente(id_cliente)
        if total >= 3:
            print("❌ Limite de 3 empréstimos atingido.")
            return False

       
        for e in self.__emprestimos:
            if e.get_id_livro() == id_livro:
                print("❌ Este livro já está emprestado.")
                return False

        if self.__emprestimos:
            novo_id = max(int(e.get_id()) for e in self.__emprestimos) + 1
        else:
            novo_id = 1

        data_inicio = date.today()
        data_entrega = data_inicio + timedelta(days=15)

        novo = Emprestimo(
            novo_id,
            id_cliente,
            id_livro,
            data_inicio.strftime("%d-%m-%Y"),  
            data_entrega.strftime("%d-%m-%Y")
        )

        self.__emprestimos.append(novo)
        self.__salvar_emprestimos()

        print(f"✅ Empréstimo criado com sucesso!")
        print(f"📘 ID: {novo_id} | Cliente: {id_cliente} | Livro: {id_livro}")
        print(f"📅 Início: {data_inicio.strftime('%d/%m/%Y')} | Devolução: {data_entrega.strftime('%d/%m/%Y')}")

        return True
    # ------------------- REMOVER EMPRÉSTIMO -------------------
    def remover_emprestimo(self, id_emprestimo, id_cliente):
        encontrado = False
        for e in self.__emprestimos:
            if e.get_id() == id_emprestimo and e.get_id_cliente() == id_cliente:
                self.__emprestimos.remove(e)
                encontrado = True
                break
        if encontrado:
            self.__salvar_emprestimos()
            print("✅ Empréstimo removido com sucesso.")
        else:
            print("❌ Empréstimo não encontrado.")

    def salvar_usuarios(self):
        caminho = os.path.join(self.__data_path, "usuarios.txt")
        with open(caminho, "w", encoding="utf-8") as f:
            for u in self.__usuarios:
                f.write(f"{u.get_id()};{u.get_nome()};{u.get_tipo()};{u.get_login()};{u.get_senha()}\n")

    def criar_usuario(self, nome, tipo, login, senha):
        novo_id = max([u.get_id() for u in self.__usuarios], default=0) + 1
        novo_usuario = Usuario(novo_id, nome, tipo, login, senha)
        self.__usuarios.append(novo_usuario)
        self.salvar_usuarios()
        print(f"✅ Usuário '{nome}' criado com sucesso! (ID {novo_id})")

    def deletar_usuario(self, id_usuario):
        for u in self.__usuarios:
            if u.get_id() == int(id_usuario):
                self.__usuarios.remove(u)
                self.salvar_usuarios()
                print(f"✅ Usuário '{u.get_nome()}' removido com sucesso!")
                return
        print("❌ Usuário não encontrado.")


    # ==============================
    # 🔹 CRUD DE LIVROS
    # ==============================
    def salvar_livros(self):
        caminho = os.path.join(self.__data_path, "livros.txt")
        with open(caminho, "w", encoding="utf-8") as f:
            for l in self.__livros:
                f.write(f"{l.get_id()};{l.get_titulo()};{l.get_autor()}\n")

    def criar_livro(self, titulo, autor):
        novo_id = max([l.get_id() for l in self.__livros], default=0) + 1
        novo_livro = Livro(novo_id, titulo, autor)
        self.__livros.append(novo_livro)
        self.salvar_livros()
        print(f"✅ Livro '{titulo}' cadastrado com sucesso! (ID {novo_id})")

    def deletar_livro(self, id_livro):
        for l in self.__livros:
            if l.get_id() == int(id_livro):
                self.__livros.remove(l)
                self.salvar_livros()
                print(f"✅ Livro '{l.get_titulo()}' removido com sucesso!")
                return
        print("❌ Livro não encontrado.") 

