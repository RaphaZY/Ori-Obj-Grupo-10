from model.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, id=None, nome=None, cpf=None, endereco=None, data_nascimento=None, telefone=None, email=None, sexo=None, matricula=None, ano_inicio=None, turmas=None, cursos=None):
        super().__init__(id,nome, cpf, endereco, data_nascimento, telefone, email, sexo)
        self.__matricula = matricula
        self.__ano_inicio = ano_inicio
        self.__turmas = turmas or []
        self.__cursos = cursos or []


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
        for turma in self.__turmas:
            return turma

    def add_curso(self, curso):
        self.__cursos.append(curso)

    def get_cursos(self):
        for curso in self.__cursos:
            return curso
        
    def remove_turma(self, turma):
        if turma in self.__turmas:
            self.__turmas.remove(turma)
            return True
        
    def remove_curso(self, curso):
        if curso in self.__cursos:
            self.__cursos.remove(curso)
            return True

    def imprimir_dados(self):
        super().imprimir_dados()
        print(f"|Matricula: {self.get_matricula()}\n"
              f"|Ano de Início: {self.get_ano_inicio()}\n"
              f"|Turmas: {self.get_turmas()}\n"
              f"|cursos: {self.get_cursos()}\n"
              )
