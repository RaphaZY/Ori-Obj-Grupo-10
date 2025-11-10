from model.trasacao import Transacao

class Compra(Transacao):
    def __init__(self, dataCompra=None, produto=None, fornecedor=None, qtdeCompra=None, precoUnit=None):
        super().__init__(dataCompra, produto, qtdeCompra)
        self.__fornecedor = fornecedor
        self.__precoUnit = precoUnit

    def get_fornecedor(self):
        return self.__fornecedor
    
    def set_fornecedor(self, fornecedor):
        self.__fornecedor = fornecedor

    def get_precoUnit(self):
        return self.__precoUnit
    
    def set_precoUnit(self, precoUnit):
        self.__precoUnit = precoUnit

    def comprar(self):
        produto = self.get_produto()
        if produto.verificarEstoqueExcedente(self.get_qtde()):
            produto.creditarEstoque(self.get_qtde())
            produto.registrarHistorico(f"Compra do produto {produto.get_nome()} - Fornecedor: {self.get_fornecedor().get_nome()} ")
            print(f"Compra do produto {produto.get_nome()} realizada com sucesso.")
            return True
        else:
            print("Erro: Estoque excedente, não é possível comprar mais.")
            return False


