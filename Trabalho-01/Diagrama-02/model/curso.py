class Curso:
    def __init__(self, id, descricao=None):
        self.__id = id
        self.__descricao = descricao
        self.__disciplinas = []

    def add_disciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

    def get_descricao(self):
        return self.__descricao
    
    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_disciplinas(self):
        for disciplina in self.__disciplinas:
            return disciplina.get_descricao()
