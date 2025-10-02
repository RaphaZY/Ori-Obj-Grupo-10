from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome=None, cpf=None, email=None, telefone=None, endereco=None, data_nascimento=None, sexo=None):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__endereco = endereco
        self.__data_nascimento = data_nascimento
        self.__sexo = sexo

    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_email(self):
        return self.__email
    
    def get_telefone(self):
        return self.__telefone
    
    def get_endereco(self):
        return self.__endereco
    
    def get_data_nascimento(self):
        return self.__data_nascimento
    
    def get_sexo(self):
        return self.__sexo
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_email(self, email):
        self.__email = email

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    def set_sexo(self, sexo):
        self.__sexo = sexo

    @abstractmethod
    def imprimir_dados(self):
        print(f'|Nome: {self.get_nome()}\n'
              f'|CPF: {self.get_cpf()}\n'
              f'|Endereço: {self.get_endereco()}\n'
              f'|Data de Nascimento: {self.get_data_nascimento()}\n'
              f'|Telefone: {self.get_telefone()}\n'
              f'|Email: {self.get_email()}\n'
              f'|Sexo: {self.get_sexo()}'
              )

    