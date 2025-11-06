from model.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, placa=None, valor=None):
        super().__init__(placa, valor)
        self.__valor = valor

    def calcular_aluguel(self, dias):
        total = self.get_valor() * dias
        if dias >= 30:
            total *= 1.10  # +10%
        else:
            total *= 1.20  # +20%
        return total