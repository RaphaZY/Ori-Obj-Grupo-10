class Funcionario:
    def __init__(self,id=None, nome=None, escolaridade=None, pais_alocacao=None):
        self.__id = id
        self.__nome = nome
        self.__escolaridade = escolaridade
        self.__pais_alocacao = pais_alocacao
        self.__departamento = None
        self.__coordenacao = None 

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome

    def get_escolaridade(self):
        return self.__escolaridade

    def get_pais_alocacao(self):
        return self.__pais_alocacao

    def get_departamento(self):
        return self.__departamento

    def get_coordenacao(self):
        return self.__coordenacao

    def set_departamento(self, departamento):
        self.__departamento = departamento

    def set_coordenacao(self, filial):
        self.__coordenacao = filial

    def set_nome(self, nome):
        self.__nome = nome

    def set_escolaridade(self, escolaridade):
        self.__escolaridade = escolaridade

    def set_pais_alocacao(self, pais_alocacao):
        self.__pais_alocacao = pais_alocacao