class Escolaridade:
    def __init__(self, nivel=None):
        self.__nivel = nivel

    def get_nivel(self):
        return self.__nivel

    def set_nivel(self, nivel):
        self.__nivel = nivel