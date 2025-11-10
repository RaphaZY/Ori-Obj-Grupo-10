from model.trasacao import Transacao

class Venda(Transacao):
    def __init__(self, dataVenda=None, cliente=None, produto=None, qtdeVenda=None):
        super().__init__(dataVenda, produto, qtdeVenda)
        self.__cliente = cliente

    def get_cliente(self):
        return self.__cliente
    
    def set_cliente(self, cliente):
        self.__cliente = cliente

    def vender(self):
        produto = self.get_produto()
        if produto.verificarEstoqueInsuficiente(self.get_qtde()):
            print("Erro: Estoque insuficiente para venda.")
            return False

        produto.debitarEstoque(self.get_qtde())
        valor = produto.calcularValorVenda(self.get_qtde())
        print(f"Valor venda = {valor}")
        produto.registrarHistorico(f"Venda do produto {produto.get_nome()} - Cliente: {self.get_cliente().get_nome()} ")

        if produto.verificarEstoqueBaixo():
            print("Estoque baixo!")

        return True
