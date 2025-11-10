from model.pessoa import Pessoa

class Fornecedor(Pessoa):
    def __init__(self, nome=None, cnpj=None):
        super().__init__(nome)
        self.__cnpj = cnpj


    def get_cnpj(self):
        return self.__cnpj
    
    def set_cnpj(self, cnpj):
        self.__cnpj = cnpj


    def listar_dados(self):
        print(f'Nome: {self.get_nome()}')
        print(f'cnpj: {self.get_cnpj()}')