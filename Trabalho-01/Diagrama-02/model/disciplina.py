class Disciplina:
    def __init__(self, id, descricao=None):
        self.__id = id
        self.__descricao = descricao

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao