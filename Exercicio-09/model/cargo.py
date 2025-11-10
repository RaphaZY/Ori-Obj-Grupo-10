from model.funcionario import Funcionario

class Cargo:
    def __init__(self, nome=None, salario_bruto=None):
        self.__nome = nome
        self.__salario_bruto = salario_bruto

    def get_nome(self):
        return self.__nome
    
    def get_salario_bruto(self):
        return self.__salario_bruto
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_salario_bruto(self, salario_bruto):
        self.__salario_bruto = salario_bruto