from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, id=None, nome=None, naturalidade=None, escolaridade=None):
        self.__nome = nome
        self.__naturalidade = naturalidade
        self.__escolaridade = escolaridade


    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_naturalidade(self):
        return self.__naturalidade
    
    def set_naturalidade(self, naturalidade):
        self.__naturalidade = naturalidade

    def get_escolaridade(self):
        return self.__escolaridade
    
    def set_escolaridade(self, escolaridade):
        self.__escolaridade = escolaridade

    @abstractmethod
    def imprimir_dados(self):
        print(f'|ID: {self.get_id()}\n'
              f'|Nome: {self.get_nome()}\n'
              f'|Naturalidade: {self.get_naturalidade()}\n'
              f'|Escolaridade: {self.get_escolaridade()}\n'
              )
