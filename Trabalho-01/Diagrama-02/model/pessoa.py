from abc import ABC, abstractmethod 

class Pessoa(ABC):
    def __init__(self, id, nome=None, cpf=None, data_nascimento=None, email=None, endereco=None, telefone=None, identidade=None):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._email = email
        self._endereco = endereco
        self._telefone = telefone
        self._identidade = identidade

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email
    
    def get_cpf(self):
        return self._cpf
    
    def get_data_nascimento(self):
        return self._data_nascimento
    
    def get_endereco(self):
        return self._endereco
    
    def get_telefone(self):
        return self._telefone
    
    def get_identidade(self):
        return self._identidade
    
    def set_nome(self, nome):
        self._nome = nome

    def set_email(self, email):
        self._email = email

    def set_cpf(self, cpf):
        self._cpf = cpf

    def set_data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento

    def set_endereco(self, endereco):
        self._endereco = endereco

    def set_telefone(self, telefone):
        self._telefone = telefone

    def set_identidade(self, identidade):
        self._identidade = identidade

    @abstractmethod
    def imprimir_dados(self):
        print(f'|Nome: {self.get_nome()}\n'
              f'|CPF: {self.get_cpf()}\n'
              f'|Email: {self.get_email()}\n'
              f'|Endereço: {self.get_endereco()}\n'
              f'|Data de Nascimento: {self.get_data_nascimento()}\n'
              f'|Telefone: {self.get_telefone()}\n'
              f'|Identidade: {self.get_identidade()}\n', end=""
              )
