class Filial:
    def __init__(self,id=None, nome=None, cidade=None, empresa=None):
        self.__id = id
        self.__nome = nome
        self.__cidade = cidade
        self.__empresa = empresa

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome

    def get_cidade(self):
        return self.__cidade

    def get_empresa(self):
        return self.__empresa

    def set_nome(self, nome):
        self.__nome = nome

    def set_cidade(self, cidade):
        self.__cidade = cidade

    def set_empresa(self, empresa):
        self.__empresa = empresa