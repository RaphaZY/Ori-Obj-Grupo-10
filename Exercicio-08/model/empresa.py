class Empresa:
    def __init__(self,id=None, nome=None, diretor=None, grupo=None):
        self.__id = id
        self.__nome = nome
        self.__diretor = diretor
        self.__grupo = grupo

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome

    def get_diretor(self):
        return self.__diretor

    def get_grupo(self):
        return self.__grupo

    def set_nome(self, nome):
        self.__nome = nome
    
    def set_diretor(self, diretor):
        self.__diretor = diretor

    def set_grupo(self, grupo):
        self.__grupo = grupo