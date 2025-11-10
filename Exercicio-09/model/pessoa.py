from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    @abstractmethod
    def imprimir_dados(self):
        pass