class Situacao:
    def __init__(self,id=None, situacao=None, ano_semestre=None):
        self.__situacao = situacao
        self.__ano_semestre = ano_semestre

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def get_situacao(self):
        return self.__situacao

    def get_ano_semestre(self):
        return self.__ano_semestre

    def set_situacao(self, situacao):
        self.__situacao = situacao

    def set_ano_semestre(self, ano_semestre):
        self.__ano_semestre = ano_semestre