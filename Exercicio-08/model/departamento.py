class Departamento:
    def __init__(self, nome=None, chefe=None):
        self.__nome = nome
        self.__chefe = chefe  

    def get_nome(self):
        return self.__nome

    def get_chefe(self):
        return self.__chefe


    def set_nome(self, nome):
        self.__nome = nome

    def set_chefe(self, chefe):
        self.__chefe = chefe