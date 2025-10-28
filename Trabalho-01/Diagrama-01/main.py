from datetime import date

from model.empresa import Empresa
from model.participante import Participante
from model.produto import Produto
from model.item_nota import ItemNota
from model.nota import Nota

def main():
    
    empresa = Empresa()
    empresa.set_id(1)
    empresa.set_codigo(101)
    empresa.set_razao_social("Tech Inova Ltda")
    empresa.set_endereco("Rua Central, 123")
    empresa.set_cnpj("11.111.111/0001-11")

    participante = Participante()
    participante.set_id(1)
    participante.set_codigo(500)
    participante.set_razao_social("Comercial Alpha")
    participante.set_cnpj("22.222.222/0001-22")

  
    produto1 = Produto()
    produto1.set_id(1)
    produto1.set_codigo("P001")
    produto1.set_descricao("Teclado Mecânico")

    produto2 = Produto()
    produto2.set_id(2)
    produto2.set_codigo("P002")
    produto2.set_descricao("Mouse Gamer")

  
    nota = Nota()
    nota.set_id(1)
    nota.set_data(date.today())
    nota.set_numero(1001)
    nota.set_empresa(empresa)
    nota.set_participante(participante)

    
    item1 = ItemNota()
    item1.set_id(1)
    item1.set_produto(produto1)
    item1.set_vr_unitario(250.00)
    item1.set_quantidade(2)

    item2 = ItemNota()
    item2.set_id(2)
    item2.set_produto(produto2)
    item2.set_vr_unitario(150.00)
    item2.set_quantidade(3)

    nota.add_item(item1)
    nota.add_item(item2)

    empresa.add_nota(nota)
    participante.add_nota(nota)

   
    print(f"Empresa: {nota.get_empresa().get_razao_social()} ")
    print(f"Participante: {nota.get_participante().get_razao_social()}")
    print(f"Número da nota: {nota.get_nota()}")
    print("\nItens da Nota:")

    for item in nota.get_itens():
        print(f"- {item.get_produto().get_descricao()} | "
            f"Qtd: {item.get_quantidade()} | "
            f"Vlr Unit: {item.get_vr_unitario():.2f} | "
            f"Total: {item.get_total():.2f}")

    print(f"\nValor total da nota: R$ {nota.get_vr_total():.2f}")


if __name__ == "__main__":
    main()
