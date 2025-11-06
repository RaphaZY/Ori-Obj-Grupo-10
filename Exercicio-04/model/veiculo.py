from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Veiculo(ABC):
    def __init__(self, placa=None, valor=None):
        self.__placa = placa
        self.__valor = valor
        self.__alugado = False
        self.__historico = []

    def get_placa(self):
        return self.__placa

    def set_placa(self, placa):
        self.__placa = placa

    def get_valor(self):
        return self.__valor
    
    def set_valor(self, valor):
        self.__valor = valor
    
    def get_alugado(self):
        return self.__alugado
    
    def set_alugado(self, alugado):
        self.__alugado = alugado

    def get_historico(self):
        return self.__historico
    
    def add_historico(self, info):
        self.__historico.append(info)


    def alugar(self, cliente, dias):
        historico_aluguel = []
        if self.__alugado:
            return f"Aluguel invalido: veículo {self.__placa} já está alugado!"
        self.__alugado = True
        valor_total = self.calcular_aluguel(dias)
        info = f"Aluguel efetuado para o cliente {cliente.get_nome()} no valor de R$ {valor_total:.2f} em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}."
        historico_aluguel.append(info)
        self.add_historico(historico_aluguel)
        return info
    
    def devolver(self, dias):
        historico_aluguel = []
        if not self.get_alugado():
            return f"Devolução invalida: veículo {self.get_placa()} não está alugado!"
        self.__alugado = False
        dia_devolucao = datetime.now() + timedelta(days=dias)
        info = f"Veículo {self.__placa} devolvido em {dia_devolucao.strftime('%d/%m/%Y %H:%M:%S')}."
        historico_aluguel.append(info)
        self.add_historico(historico_aluguel)
        return info

    def listar_historico(self):
        print(f"\nHistórico do veículo {self.__placa}:")
        for item in self.get_historico():
            print(item)

    @abstractmethod
    def calcular_aluguel(self, dias):
        pass

