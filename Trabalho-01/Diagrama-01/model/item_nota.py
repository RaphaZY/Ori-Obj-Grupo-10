from decimal import Decimal

class ItemNota:
    def __init__(self, id, produto=None, vr_unitario=None, quantidade=None):
        self.__id = id
        self.__produto = produto
        self.__vr_unitario = vr_unitario
        self.__quantidade = quantidade

    def get_produto(self):
        return self.__produto

    def get_vr_unitario(self):
        return self.__vr_unitario

    def get_quantidade(self):
        return self.__quantidade

    def get_total(self):
        return self.__vr_unitario * self.__quantidade

    def set_produto(self, produto):
        self.__produto = produto
    
    def set_vr_unitario(self, vr_unitario):
        self.__vr_unitario = Decimal(vr_unitario)

    def set_quantidade(self, quantidade):
        self.__quantidade = Decimal(quantidade)