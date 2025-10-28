from decimal import Decimal

class Nota:
    def __init__(self, id=None, data=None, numero=None, empresa=None, participante=None):
        self.__id = id
        self.__data = data
        self.__numero = numero
        self.__empresa = empresa
        self.__participante = participante
        self.__itens = []

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id


    def add_item(self, item):
        self.__itens.append(item)

    def get_itens(self):
        return self.__itens

    def get_empresa(self):
        return self.__empresa

    def get_participante(self):
        return self.__participante

    def get_vr_total(self):
        total = Decimal(0)
        for item in self.get_itens():
            total += item.get_total()
        return total

    def get_nota(self):
        return self.__numero

    def set_data(self, data):
        self.__data = data

    def set_numero(self, numero):
        self.__numero = numero

    def set_empresa(self, empresa):
        self.__empresa = empresa

    def set_participante(self, participante):
        self.__participante = participante