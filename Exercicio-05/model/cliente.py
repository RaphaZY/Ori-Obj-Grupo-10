from model.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome=None, cpf=None):
        super().__init__(nome)
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        self.__cpf = cpf

    def listar_dados(self):
        print(f'Nome: {self.get_nome()}')
        print(f'CPF: {self.get_cpf()}')
