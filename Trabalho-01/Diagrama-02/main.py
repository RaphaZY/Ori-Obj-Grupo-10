from datetime import date
from model.aluno import Aluno
from model.professor import Professor
from model.disciplina import Disciplina
from model.curso import Curso
from model.turma import Turma
from model.diario import Diario
from model.situacao import Situacao
from model.instituicao import Instituicao


def main():
    inst = Instituicao()
    inst.set_id(1)
    inst.set_descricao("Universidade Federal da Tecnologia")

    curso = Curso()
    curso.set_id(1)
    curso.set_descricao("Engenharia de Software")

    disciplina = Disciplina()
    disciplina.set_id(1)
    disciplina.set_descricao("Programação Orientada a Objetos")

    professor = Professor()
    professor.set_id(1)
    professor.set_nome("Dr. Marcos Lima")
    professor.set_cpf("123456789-00")
    professor.set_data_nascimento(date(1980, 5, 10))
    professor.set_email("marcos@uft.edu")
    professor.set_endereco("Rua A, 123")
    professor.set_telefone("99999-9999")
    professor.set_identidade("MG123456")
    professor.set_matricula("P001")
    professor.set_titulacao_maxima("Doutorado")

    aluno = Aluno()
    aluno.set_id(1)
    aluno.set_nome("Ana Souza")
    aluno.set_cpf("987654321-00")
    aluno.set_data_nascimento(date(2002, 8, 15))
    aluno.set_email("ana@email.com")
    aluno.set_endereco("Rua B, 456")
    aluno.set_telefone("98888-8888")
    aluno.set_identidade("SP654321")
    aluno.set_matricula("A001")
    aluno.set_ano_inicio(2021)
    aluno.set_semestre_inicio(1)

    turma = Turma()
    turma.set_id(1)
    turma.set_descricao("Turma A")
    turma.set_ano(2024)
    turma.set_semestre(2)


    diario = Diario()
    diario.set_id(1)
    notas = "8.5, 7.0, 9.0, 8.0"
    diario.set_faltas(2)
    diario.set_notas(notas)

    situacao = Situacao()
    situacao.set_id(1)
    situacao.set_situacao("Matriculado")
    situacao.set_ano_semestre("2024/2")

    
    inst.add_curso(curso)
    curso.add_disciplina(disciplina)
    turma.set_disciplina(disciplina)
    turma.add_diario(diario)
    aluno.add_diario(diario)
    aluno.add_situacao(situacao)
    professor.add_curso(curso)

    print("\n|--------------------------------------")
    print(f"|Instituição: {inst.get_descricao()}")
    print(f"|Curso: {curso.get_descricao()}")
    print(f"|Disciplinas: {curso.get_disciplinas()}")
    print("\n--------Professor----------")
    professor.imprimir_dados()
    print("---------Aluno------------")
    aluno.imprimir_dados()
    print(f"Situação: {aluno.get_situacoes()} - {aluno.get_situacoes_ano_semestre()}")
    print(f"Média final: {aluno.get_diarios()}")
    print(f"Faltas: {aluno.get_diarios_faltas()}")


if __name__ == "__main__":
    main()