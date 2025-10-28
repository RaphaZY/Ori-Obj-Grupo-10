class Pais:
    def __init__(self,id=None, nome=None):
        self.__id = id
        self.__nome = nome

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
