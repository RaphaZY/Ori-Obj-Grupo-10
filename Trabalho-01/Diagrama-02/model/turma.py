class Turma:
    def __init__(self, id, descricao=None, ano=None, semestre=None):
        self.__id = id
        self.__descricao = descricao
        self.__ano = ano
        self.__semestre = semestre
        self.__diarios = []
        self.__disciplina = None

    def add_diario(self, diario):
        self.__diarios.append(diario)

    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina

    def get_descricao(self):
        return self.__descricao
    
    def get_ano(self):
        return self.__ano
    
    def get_semestre(self):
        return self.__semestre
    
    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_ano(self, ano):
        self.__ano = ano

    def set_semestre(self, semestre):
        self.__semestre = semestre
