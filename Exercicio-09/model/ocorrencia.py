from datetime import datetime
from model.funcionario import Funcionario

class Ocorrencia:
    def __init__(self, data_ocorrencia=None, valor=None, descricao=None):
        self.__data_ocorrencia = data_ocorrencia
        self.__valor = valor
        self.__descricao = descricao

    def get_data_ocorrencia(self):
        return self.__data_ocorrencia

    def get_valor(self):
        return self.__valor
    
    def get_descricao(self):
        return self.__descricao
    
    def set_data_ocorrencia(self, data_ocorrencia):
        self.__data_ocorrencia = datetime.strptime(data_ocorrencia, '%d/%m/%Y')
        
    def set_valor(self, valor):
        self.__valor = valor

    def set_descricao(self, descricao):
        self.__descricao = descricao