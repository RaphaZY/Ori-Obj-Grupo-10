from model.escolaridade import Escolaridade
from model.estado import Estado
from model.cidade import Cidade
from model.tipo_ensino import TipoEnsino
from model.professor import Professor
from model.aluno import Aluno
from model.curso import Curso
from model.escola import Escola

def main():
    superior = TipoEnsino()
    superior.set_id(1)
    superior.set_descricao("Ensino Superior")

    medio = TipoEnsino()
    medio.set_id(2)
    medio.set_descricao("Ensino Médio")

    e1 = Escolaridade()
    e1.set_id(1)
    e1.set_descricao("Mestrado")

    e2 = Escolaridade()
    e2.set_id(2)
    e2.set_descricao("Doutorado")

    e3 = Escolaridade()
    e3.set_id(3)
    e3.set_descricao("Graduação")

    estado_sp = Estado()
    estado_sp.set_id(1)
    estado_sp.set_nome("São Paulo")

    cidade_sp = Cidade()
    cidade_sp.set_id(1)
    cidade_sp.set_nome("São Paulo")
    cidade_sp.set_estado(estado_sp)

    cidade_campinas = Cidade()
    cidade_campinas.set_id(2)
    cidade_campinas.set_nome("Campinas")
    cidade_campinas.set_estado(estado_sp)   

    professor1 = Professor()
    professor1.set_id(1)
    professor1.set_nome("Carlos")
    professor1.set_naturalidade(cidade_sp)
    professor1.set_escolaridade(e1)
    professor1.set_tipo_ensino(superior)

    professor2 = Professor()
    professor2.set_id(2)
    professor2.set_nome("Maria")
    professor2.set_naturalidade(cidade_campinas)
    professor2.set_escolaridade(e2)
    professor2.set_tipo_ensino(medio)

    curso_ads = Curso()
    curso_ads.set_id(1)
    curso_ads.set_nome("Análise e Desenvolvimento de Sistemas")
    curso_ads.set_tipo_ensino(superior)
    curso_ads.set_coordenador(coordenador=professor1)
    curso_ads.add_professor(professor1)


    aluno1 = Aluno()
    aluno1.set_id(1)
    aluno1.set_nome("João")
    aluno1.set_escolaridade(e3)
    aluno1.add_curso(curso_ads)
    aluno1.set_naturalidade(cidade_campinas)

    escola = Escola()
    escola.set_id(1)
    escola.set_nome("Faculdade XPTO")
    escola.set_cidade(cidade_sp)
    escola.set_diretor(professor2)
    escola.add_cursos(curso_ads)

    curso_ads.add_aluno(aluno1)
    curso_ads.set_escola(escola)

    print("a)", professor1.get_escolaridade().get_descricao())
    print("b)", curso_ads.get_coordenador().get_escolaridade().get_descricao())
    print("c)", escola.get_diretor().get_escolaridade().get_descricao())
    print("d)", aluno1.get_naturalidade().get_estado().get_nome())
    print("e)", professor1.get_naturalidade().get_nome())
    print("f)", aluno1.get_curso()[0].get_escola().get_cidade().get_estado().get_nome())
    print("g)", professor1.get_tipo_ensino().get_descricao())
    print("h)", aluno1.get_curso()[0].get_coordenador().get_nome())
    print("i)", escola.get_diretor().get_nome())
    print("j)", curso_ads.get_coordenador().get_nome())

if __name__ == "__main__":
    main()
