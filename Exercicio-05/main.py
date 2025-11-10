from model.cliente import Cliente
from model.fornecedor import Fornecedor
from model.compra import Compra
from model.venda import Venda
from model.trasacao import Transacao
from model.produto import Produto

def main():
    
    cliente1 = Cliente()
    cliente1.set_nome("João")
    cliente1.set_cpf("123.456.789-00")

    cliente2 = Cliente()
    cliente2.set_nome("Maria")
    cliente2.set_cpf("444.456.741-00")


    fornecedor1 = Fornecedor()
    fornecedor1.set_nome("Fornecedor 1")
    fornecedor1.set_cnpj("12.345.678/0001-00")

    fornecedor2 = Fornecedor()
    fornecedor2.set_nome("Fornecedor 2")
    fornecedor2.set_cnpj("12.888.678/9990-00")


    produto1 = Produto()
    produto1.set_nome("Livro")
    produto1.set_estoque(70)
    produto1.set_precoUnit(20.00)
    produto1.set_estoqueMinimo(10)
    produto1.set_estoqueMaximo(100)

    produto2 = Produto()
    produto2.set_nome("Caneta")
    produto2.set_estoque(450)
    produto2.set_precoUnit(1.75)
    produto2.set_estoqueMinimo(100)
    produto2.set_estoqueMaximo(1000)

    print("\n----------Compra do produto Livro------------")
    compra1 = Compra()
    compra1.set_dataTransacao("26/07/2021")
    compra1.set_produto(produto1)
    compra1.set_fornecedor(fornecedor1)
    compra1.set_precoUnit(11.1)
    compra1.set_qtde(25)
    compra1.comprar()

    print("\n----------Compra do produto Caneta------------")
    compra2 = Compra()
    compra2.set_dataTransacao("26/07/2021")
    compra2.set_produto(produto2)
    compra2.set_fornecedor(fornecedor2)
    compra2.set_precoUnit(1.5)
    compra2.set_qtde(250)
    compra2.comprar()

    print("\n----------Venda do produto Livro------------")
    venda1 = Venda()
    venda1.set_dataTransacao("26/07/2021")
    venda1.set_cliente(cliente1)
    venda1.set_produto(produto1)
    venda1.set_qtde(45)
    venda1.vender()

    
    venda2 = Venda()
    venda2.set_dataTransacao("26/08/2021")
    venda2.set_cliente(cliente1)
    venda2.set_produto(produto1)
    venda2.set_qtde(45)
    venda2.vender()

    print("\n----------Venda do produto Caneta------------")

    venda3 = Venda()
    venda3.set_dataTransacao("26/07/2021")
    venda3.set_cliente(cliente2)
    venda3.set_produto(produto2)
    venda3.set_qtde(4)
    venda3.vender()

    venda4 = Venda()
    venda4.set_dataTransacao("26/07/2021")
    venda4.set_cliente(cliente1)
    venda4.set_produto(produto2)
    venda4.set_qtde(90)
    venda4.vender()

    print("\n----------------------")
    produto1.exibirHistorico()
    print("\n----------------------")
    produto2.exibirHistorico()


if __name__ == "__main__":
    main()