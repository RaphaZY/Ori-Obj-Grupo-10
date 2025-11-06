from datetime import datetime
from model.cliente import Cliente
from model.carro import Carro
from model.moto import Moto


def main():

    cliente1=Cliente()
    cliente1.set_nome("Marcos")
    cliente1.set_cpg("123.456.789-00")
    cliente1.set_telefone("9999-9999")

    cliente2=Cliente()
    cliente2.set_nome("Antônio")
    cliente2.set_cpg("987.654.321-00")
    cliente2.set_telefone("8888-8888")

    carro1=Carro()
    carro1.set_modelo("Celta")
    carro1.set_placa("ABC123")
    carro1.set_valor(100)

    carro2=Carro()
    carro2.set_modelo("Uno")
    carro2.set_placa("XYZ456")
    carro2.set_valor(80)

    moto1=Moto()
    moto1.set_placa('MOT123')
    moto1.set_valor(40)

    moto2=Moto()
    moto2.set_placa('MOT234')
    moto2.set_valor(50)

    print("===============================")
    print(carro1.alugar(cliente1,10))
    print(carro1.devolver(10))
    print(carro1.alugar(cliente2,15))

    print("\n==========Historico============")
    carro1.listar_historico()
    print("===============================\n")

    print(carro2.devolver(10))

    print("\n===============================")
    print(moto1.alugar(cliente1,20))
    print(moto1.devolver(20))
    print(moto1.alugar(cliente2,30))
    
    print("\n==========Historico============")
    moto1.listar_historico()
    print("===============================\n")


if __name__ == "__main__":
    main()













