from model.pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome=None, cpf=None, email=None, telefone=None, endereco=None, data_nascimento=None, sexo=None, matricula=None, salario=None, turmas=None):
        super().__init__(nome, cpf, email, telefone, endereco, data_nascimento, sexo)
        self.__salario = salario
        self.__matricula = matricula
        self.__turmas = turmas or []

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_matricula(self):
        return self.__matricula
    
    def set_salario(self, salario):
        self.__salario = salario

    def get_salario(self):
        return self.__salario
    
    def add_turma(self, turma):
        self.__turmas.append(turma)

    def get_turmas(self):
        lista = []
        for turma in self.__turmas:
            lista.append(turma.get_id())
        return lista
    
    def imprimir_dados(self):
        super().imprimir_dados()
        print(f"|Matricula: {self.get_matricula()}\n"
            f"|Salário: {self.get_salario()}\n"
            f"|Turmas: {self.get_turmas()}\n")
        