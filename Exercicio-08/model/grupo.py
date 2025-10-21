class Grupo:
    def __init__(self, nome=None, presidente=None, sede=None):
        self.__nome = nome
        self.__presidente = presidente
        self.__sede = sede  

    def get_nome(self):
        return self.__nome

    def get_presidente(self):
        return self.__presidente

    def get_sede(self):
        return self.__sede
    
    def set_presidente(self, presidente):
        self.__presidente = presidente

    def set_sede(self, sede):
        self.__sede = sede

    def set_nome(self, nome):
        self.__nome = nome
