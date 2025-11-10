from datetime import datetime

class Transacao:
    def __init__(self, dataTransacao=None, produto=None, qtde=None):
        self.__dataTransacao = dataTransacao
        self.__produto = produto
        self.__qtde = qtde

    def get_dataTransacao(self):
        return self.__dataTransacao
    
    def set_dataTransacao(self, dataTransacao):
        if isinstance(dataTransacao, datetime):
            self.__dataTransacao = dataTransacao.strftime('%d/%m/%Y')
        else:
            self.__dataTransacao = dataTransacao

    def get_produto(self):
        return self.__produto

    def set_produto(self, produto):
        self.__produto = produto

    def get_qtde(self):
        return self.__qtde

    def set_qtde(self, qtde):
        self.__qtde = qtde