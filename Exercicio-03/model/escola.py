class Escola:
    def __init__(self,id=None, nome=None, cidade=None, diretor=None, cursos=None):
        self.__id = id
        self.__nome = nome
        self.__cidade = cidade
        self.__diretor = diretor
        self.__cursos = cursos or []

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id  

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_cidade(self):
        return self.__cidade
    
    def set_cidade(self, cidade):
        self.__cidade = cidade

    def get_diretor(self):
        return self.__diretor
    
    def set_diretor(self, diretor):
        self.__diretor = diretor

    def get_cursos(self):
        return self.__cursos
    
    def add_cursos(self, cursos):
        self.__cursos.append(cursos)