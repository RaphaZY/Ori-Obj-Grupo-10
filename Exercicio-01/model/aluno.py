from model.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome=None, cpf=None, endereco=None, data_nascimento=None, telefone=None, email=None, sexo=None, matricula=None, ano_inicio=None, turmas=None, diciplinas=None):
        super().__init__(nome, cpf, endereco, data_nascimento, telefone, email, sexo)
        self.__matricula = matricula
        self.__ano_inicio = ano_inicio
        self.__turmas = turmas or []
        self.__diciplinas = diciplinas or []


    def get_matricula(self):
        return self.__matricula
    
    def get_ano_inicio(self):
        return self.__ano_inicio
    
    
    def set_matricula(self, matricula):
        self.__matricula = matricula

    def set_ano_inicio(self, ano_inicio):
        self.__ano_inicio = ano_inicio

    def add_turma(self, turma):
        self.__turmas.append(turma)

    def get_turmas(self):
        lista_turmas = []
        for turma in self.__turmas:
            lista_turmas.append(turma.get_id())
        return lista_turmas

    def add_diciplina(self, diciplina):
        self.__diciplinas.append(diciplina)

    def get_diciplinas(self):
        lista_diciplinas = []
        for diciplina in self.__diciplinas:
            lista_diciplinas.append(diciplina.get_nome())
        return lista_diciplinas

    def imprimir_dados(self):
        super().imprimir_dados()
        print(f"|Matricula: {self.get_matricula()}\n"
              f"|Ano de Início: {self.get_ano_inicio()}\n"
              f"|Turmas: {self.get_turmas()}\n"
              f"|Diciplinas: {self.get_diciplinas()}\n"
              )
