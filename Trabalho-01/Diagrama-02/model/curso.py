class Curso:
    def __init__(self, id=None, descricao=None):
        self.__id = id
        self.__descricao = descricao
        self.__disciplinas = []

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def add_disciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

    def get_descricao(self):
        return self.__descricao
    
    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_disciplinas(self):
        for disciplina in self.__disciplinas:
            return disciplina.get_descricao()
