from model.escolaridade import Escolaridade
from model.estado import Estado
from model.cidade import Cidade
from model.tipo_ensino import TipoEnsino
from model.professor import Professor
from model.aluno import Aluno
from model.curso import Curso
from model.escola import Escola

def main():
    superior = TipoEnsino("Ensino Superior")
    medio = TipoEnsino("Ensino Médio")

    e1 = Escolaridade("Mestrado")
    e2 = Escolaridade("Doutorado")
    e3 = Escolaridade("Graduação")

    estado_sp = Estado("São Paulo")
    cidade_sp = Cidade("São Paulo", estado_sp)
    cidade_campinas = Cidade("Campinas", estado_sp)

    professor1 = Professor("Carlos", cidade_sp, e1, superior)
    professor2 = Professor("Mariana", cidade_campinas, e2, medio)

    curso_ads = Curso("Análise e Desenvolvimento de Sistemas", superior, coordenador=professor1)
    aluno1 = Aluno("João", cidade_campinas, e3, curso_ads)

    escola = Escola("Faculdade XPTO", cidade_sp, diretor=professor2)

    print("a)", professor1.escolaridade.descricao)
    print("b)", curso_ads.coordenador.escolaridade.descricao)
    print("c)", escola.diretor.escolaridade.descricao)
    print("d)", aluno1.naturalidade.estado.nome)
    print("e)", professor1.naturalidade.nome)
    print("f)", aluno1.naturalidade.estado.nome)
    print("g)", professor1.tipo_ensino.descricao)
    print("h)", aluno1.curso.coordenador.nome)
    print("i)", escola.diretor.nome)
    print("j)", curso_ads.coordenador.nome)

if __name__ == "__main__":
    main()
