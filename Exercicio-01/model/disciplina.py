class Disciplina():

    def __init__(self, id=None, nome=None, turmas=None, professores=None):
        self.__id = id
        self.__nome = nome
        self.__turmas = turmas or []
        self.__professores = professores or []

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome 
    
    def add_turma(self, turma):
        self.__turmas.append(turma)
    
    def get_turmas(self):
        return [turma.get_id() for turma in self.__turmas]

    def get_id(self):
        return self.__id   
    
    def set_id(self, id):
        self.__id = id

    def add_professor(self, professor):
        self.__professores.append(professor)

    def get_professores(self):
        return self.__professores