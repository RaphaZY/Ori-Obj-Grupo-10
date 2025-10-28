class Curso:
    def __init__(self, id=None, nome=None, tipo_ensino=None, coordenador=None, alunos=None, professores=None, escola=None):
        self.__id = id
        self.__nome = nome
        self.__tipo_ensino = tipo_ensino
        self.__coordenador = coordenador
        self.__alunos = alunos or []
        self.__professores = professores or []
        self.__escola = escola or []

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def get_coordenador(self):
        return self.__coordenador
    
    def set_coordenador(self, coordenador):
        self.__coordenador = coordenador

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
        

    def get_tipo_ensino(self):
        return self.__tipo_ensino
    
    def set_tipo_ensino(self, tipo_ensino):
        self.__tipo_ensino = tipo_ensino

    def get_alunos(self):
        return self.__alunos
    
    def add_aluno(self, aluno):
        self.__alunos.append(aluno)

    def get_professores(self):
        return self.__professores
    
    def add_professor(self, professor):
        self.__professores.append(professor)

    def get_escola(self):
        return self.__escola
    
    def set_escola(self, escola):
        self.__escola = escola
        
