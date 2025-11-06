from model.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo=None, placa=None, valor=None):
        super().__init__(placa, valor)
        self.__modelo = modelo
        self.__valor = valor

    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self, modelo):
        self.__modelo = modelo

    def calcular_aluguel(self, dias):
        return self.get_valor() * dias