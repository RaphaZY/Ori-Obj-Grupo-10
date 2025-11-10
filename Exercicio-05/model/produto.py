class Produto:
    def __init__(self, nome=None, precoUnit=None, estoque=None, estoqueMinimo=None, estoqueMaximo=None):
        self.__nome = nome
        self.__precoUnit = precoUnit
        self.__estoque = estoque
        self.__estoqueMinimo = estoqueMinimo
        self.__estoqueMaximo = estoqueMaximo
        self.__historico = []

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_precoUnit(self):
        return self.__precoUnit
    
    def set_precoUnit(self, precoUnit):
        self.__precoUnit = precoUnit

    def get_estoque(self):
        return self.__estoque
    
    def set_estoque(self, estoque):
        self.__estoque = estoque

    def get_estoqueMinimo(self):
        return self.__estoqueMinimo
    
    def set_estoqueMinimo(self, estoqueMinimo):
        self.__estoqueMinimo = estoqueMinimo

    def get_estoqueMaximo(self):
        return self.__estoqueMaximo
    
    def set_estoqueMaximo(self, estoqueMaximo):
        self.__estoqueMaximo = estoqueMaximo

    def get_historico(self):
        return self.__historico
    
    def add_historico(self, info):
        self.__historico.append(info)

    def debitarEstoque(self, quantidade):
        self.__estoque -= quantidade

    def creditarEstoque(self, quantidade):
        self.__estoque += quantidade

    def verificarEstoqueBaixo(self):
        return self.__estoque < self.__estoqueMinimo

    def verificarEstoqueInsuficiente(self, quantidade):
        return quantidade > self.__estoque

    def verificarEstoqueExcedente(self, quantidade):
        return int(self.__estoque + quantidade) <= int(self.__estoqueMaximo)

    def calcularValorVenda(self, quantidade):
        return self.__precoUnit * quantidade

    def registrarHistorico(self, descricao):
        self.add_historico(descricao)

    def exibirHistorico(self):
        print(f"\nHistórico do produto {self.__nome}:")
        for h in self.__historico:
            print(f"- {h}")
