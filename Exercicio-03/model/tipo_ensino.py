class TipoEnsino:
    def __init__(self, id=None, descricao=None):
        self.__descricao = descricao

    def get_descricao(self):
        return self.__descricao
    
    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id