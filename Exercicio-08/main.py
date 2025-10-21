from model.grupo import Grupo
from model.pais import Pais
from model.estado import Estado
from model.cidade import Cidade
from model.empresa import Empresa
from model.departamento import Departamento
from model.funcionario import Funcionario
from model.escolaridade import Escolaridade
from model.filial import Filial

def main():
    pais_brasil = Pais()
    pais_brasil.set_nome("Brasil")

    estado_sp = Estado()
    estado_sp.set_nome("São Paulo")

    cidade_sp = Cidade()
    cidade_sp.set_nome("São Paulo")
    cidade_sp.set_estado(estado_sp)


    esc_presidente = Escolaridade()
    esc_presidente.set_nivel("Doutorado")
    esc_chefe = Escolaridade()
    esc_chefe.set_nivel("Mestrado")
    esc_funcionario = Escolaridade()
    esc_funcionario.set_nivel("Ensino Superior Completo")


    presidente = Funcionario()
    presidente.set_nome("Carlos Silva")
    presidente.set_escolaridade(esc_presidente)
    presidente.set_pais_alocacao(pais_brasil)

    chefe = Funcionario()
    chefe.set_nome("Mariana Costa")
    chefe.set_escolaridade(esc_chefe)
    chefe.set_pais_alocacao(pais_brasil)

    funcionario = Funcionario()
    funcionario.set_nome("João Souza")
    funcionario.set_escolaridade(esc_funcionario)
    funcionario.set_pais_alocacao(pais_brasil)


    grupo = Grupo()
    grupo.set_nome("NetLab")
    grupo.set_presidente(presidente)
    grupo.set_sede(pais_brasil)


    empresa = Empresa()
    empresa.set_nome("InovaTech")
    empresa.set_diretor("Pedro Lima")
    empresa.set_grupo(grupo)


    departamento = Departamento()
    departamento.set_nome("TI")
    departamento.set_chefe(chefe)


    filial = Filial()
    filial.set_nome("InovaTech SP")
    filial.set_cidade(cidade_sp)
    filial.set_empresa(empresa)


    funcionario.set_departamento(departamento)
    funcionario.set_coordenacao(filial)

    print("\n1) Escolaridade do presidente de um grupo:")
    print(grupo.get_presidente().get_escolaridade().get_nivel())

    print("\n2) País de alocação de um funcionário:")
    print(funcionario.get_pais_alocacao().get_nome())

    print("\n3) Estado da filial que um funcionário coordena:")
    print(funcionario.get_coordenacao().get_cidade().get_estado().get_nome())

    print("\n4) Escolaridade do chefe de um departamento:")
    print(funcionario.get_departamento().get_chefe().get_escolaridade().get_nivel())

    print("\n5) Nome do diretor da empresa de uma filial:")
    print(funcionario.get_coordenacao().get_empresa().get_diretor())


if __name__ == '__main__':
            
    main()
