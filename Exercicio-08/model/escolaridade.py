class Escolaridade:
    def __init__(self, id=None, nivel=None):
        self.__id = id
        self.__nivel = nivel

    def get_id(self):
        return self.__id
        
    def set_id(self, id):
        self.__id = id

    def get_nivel(self):
        return self.__nivel

    def set_nivel(self, nivel):
        self.__nivel = nivel