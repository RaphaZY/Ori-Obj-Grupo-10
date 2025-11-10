from datetime import datetime
from model.funcionario import Funcionario
from model.dependente import Dependente
from model.ocorrencia import Ocorrencia
from model.cargo import Cargo

def main():

    cargo = Cargo()
    cargo.set_nome("Analista de Sistemas")
    cargo.set_salario_bruto(5000.0)


    funcionario = Funcionario()
    funcionario.set_nome("John")
    funcionario.set_cargo(cargo)

    dependente1 = Dependente()
    dependente1.set_nome("Joaquim")
    dependente1.set_data_nascimento("15/04/2010")

    dependente2 = Dependente()
    dependente2.set_nome("Maria")
    dependente2.set_data_nascimento("10/09/2000")

    funcionario.adicionar_dependente(dependente1)
    funcionario.adicionar_dependente(dependente2)


    ocorrencia1 = Ocorrencia()
    ocorrencia1.set_data_ocorrencia("10/11/2025")
    ocorrencia1.set_valor(500.0)
    ocorrencia1.set_descricao("Bônus")

    ocorrencia2 = Ocorrencia()
    ocorrencia2.set_data_ocorrencia("12/11/2025")
    ocorrencia2.set_valor(-300.0)
    ocorrencia2.set_descricao("Desconto por atraso")

    funcionario.adicionar_ocorrencia(ocorrencia1)
    funcionario.adicionar_ocorrencia(ocorrencia2)


    salario_liquido = funcionario.calcular_salario(2025, 11)
    print(f"\nSalário líquido de {funcionario.get_nome()} (11/2025): R$ {salario_liquido:.2f}")

    funcionario.listar_dependentes()


if __name__ == "__main__":
    main()