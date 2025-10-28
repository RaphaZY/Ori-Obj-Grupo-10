from model.professor import Professor
from model.aluno import Aluno
from model.turma import Turma
from model.disciplina import Disciplina
from model.curso import Curso
from datetime import datetime

def main():

    professor1 = Professor()
    professor2 = Professor()
    aluno1 = Aluno()
    aluno2 = Aluno()
    aluno3 = Aluno()
    turma1 = Turma()
    turma2 = Turma()
    turma3 = Turma()
    disciplina1 = Disciplina()
    disciplina2 = Disciplina()
    disciplina3 = Disciplina()
    curso1 = Curso()

    professor1.set_id(1)
    professor1.set_nome("Marcos")
    professor1.set_cpf("123.456.789-00")
    professor1.set_endereco("Rua 1") 
    professor1.set_data_nascimento(datetime.strptime("01/01/1970", "%d/%m/%Y"))
    professor1.set_telefone("1234-5678")
    professor1.set_email("marcos@example.com")
    professor1.set_sexo("M")
    professor1.set_matricula("12345")
    professor1.set_salario(1618)

    professor2.set_id(2)
    professor2.set_nome("Igor")
    professor2.set_cpf("324.213.674-55")
    professor2.set_endereco("Rua 4")
    professor2.set_data_nascimento(datetime.strptime("02/11/1964", "%d/%m/%Y"))
    professor2.set_telefone("1234-5678")
    professor2.set_email("igor@example.com")
    professor2.set_sexo("M")
    professor2.set_matricula("54321")
    professor2.set_salario(1600)

    aluno1.set_id(1)
    aluno1.set_nome("João")
    aluno1.set_cpf("123.456.789-00")
    aluno1.set_endereco("Rua 1")
    aluno1.set_data_nascimento(datetime.strptime("01/01/2000", "%d/%m/%Y"))
    aluno1.set_telefone("1234-5678")
    aluno1.set_email("joao@example.com")
    aluno1.set_sexo("M")
    aluno1.set_matricula("14789")
    aluno1.set_ano_inicio(2021)

    aluno2.set_id(2)
    aluno2.set_nome("Pedro")
    aluno2.set_cpf("987.150.789-00")
    aluno2.set_endereco("Rua 3")
    aluno2.set_data_nascimento(datetime.strptime("14/08/2002", "%d/%m/%Y"))
    aluno2.set_telefone("1234-5678")
    aluno2.set_email("pedro@example.com")
    aluno2.set_sexo("M")
    aluno2.set_matricula("98574")
    aluno2.set_ano_inicio(2021)

    aluno3.set_id(3)
    aluno3.set_nome("Maria")
    aluno3.set_cpf("145.865.789-88")
    aluno3.set_endereco("Rua 5")
    aluno3.set_data_nascimento(datetime.strptime("25/07/2001", "%d/%m/%Y"))
    aluno3.set_telefone("1234-5678")
    aluno3.set_email("maria@example.com")
    aluno3.set_sexo("F")
    aluno3.set_matricula("65489")
    aluno3.set_ano_inicio(2020)

    disciplina1.set_id(1)
    disciplina1.set_nome("Matemática")
    disciplina2.set_id(2)
    disciplina2.set_nome("BD")
    disciplina3.set_id(3)    
    disciplina3.set_nome("Programação")

    turma1.set_id(1)
    turma1.set_descricao("Turma 1")
    turma1.set_professor(professor1)
    turma1.add_aluno(aluno1)
    turma1.add_aluno(aluno2)
    turma1.add_aluno(aluno3)
    turma1.set_disciplina(disciplina1)

    turma2.set_id(2)
    turma2.set_descricao("Turma 2")
    turma2.set_professor(professor1)
    turma2.add_aluno(aluno2)
    turma2.add_aluno(aluno3)
    turma2.set_disciplina(disciplina2)

    turma3.set_id(3)
    turma3.set_descricao("Turma 3")
    turma3.set_professor(professor2)
    turma3.add_aluno(aluno1)
    turma3.add_aluno(aluno3)
    turma3.set_disciplina(disciplina3)

    curso1.set_id(1)
    curso1.set_nome("Ciência da Computação")
    curso1.set_descricao("Curso de Ciência da Computação")
    curso1.add_turma(turma1)
    curso1.add_turma(turma2)
    curso1.add_turma(turma3)
    curso1.add_aluno(aluno1)
    curso1.add_aluno(aluno2)
    curso1.add_aluno(aluno3)

    turma1.set_curso(curso1)
    turma2.set_curso(curso1)
    turma3.set_curso(curso1)

    professor1.add_turma(turma1)
    professor1.add_turma(turma2)
    professor1.add_diciplina(disciplina1)
    professor1.add_diciplina(disciplina2)

    professor2.add_turma(turma3)
    professor2.add_diciplina(disciplina3)

    disciplina1.add_professor(professor1)
    disciplina2.add_professor(professor1)
    disciplina3.add_professor(professor2)

    aluno1.add_turma(turma1)
    aluno1.add_turma(turma3)

    aluno2.add_turma(turma1)
    aluno2.add_turma(turma2)

    aluno3.add_turma(turma1)
    aluno3.add_turma(turma2)
    aluno3.add_turma(turma3)

    aluno1.add_curso(curso1)
    aluno2.add_curso(curso1)
    aluno3.add_curso(curso1)

    # print('----------Dados-----------')
    # professor1.imprimir_dados()
    # print('----------------------')
    # aluno1.imprimir_dados()
    # print('----------------------')
    # aluno2.imprimir_dados()
    # print('----------------------')
    # turma1.imprimir_dados()
    # print('----------------------')
    # turma2.imprimir_dados()
    # print('----------------------')
    # print(curso1)
    # print('----------------------')

    print('----------01------------')
    print(turma1.get_professor().get_nome())

    print('----------02------------')
    for aluno in turma2.get_alunos():
        print(aluno.get_nome(), end=", ")

    print('\n----------03------------')
    print(curso1.get_turmas()[0].get_professor().get_nome())

    print('----------04------------')
    for aluno in curso1.get_turmas()[2].get_alunos():
        print(aluno.get_nome(), end=", ")

    print('\n----------05------------')
    for aluno in curso1.get_alunos():
        print(aluno.get_nome(), end=", ")

    print('\n----------06------------')
    print(curso1.get_turmas()[1].get_disciplina().get_nome())

    print('----------07------------')
    print(aluno1 in turma3.get_alunos())

    print('----------08------------')
    print(aluno3 in curso1.get_alunos())

    print('----------09------------')
    print(turma1 in curso1.get_turmas())

    print('----------10------------')
    print("Antes:", [aluno.get_nome() for aluno in turma1.get_alunos()])
    turma1.remove_aluno(aluno1)
    aluno1.remove_turma(turma1)
    print("Depois:", [aluno.get_nome() for aluno in turma1.get_alunos()])

    print('----------11------------')
    print("Antes:", [turma.get_id() for turma in curso1.get_turmas()])
    curso1.remove_turma(turma3)
    print("Depois:", [turma.get_id() for turma in curso1.get_turmas()])

    print('----------12------------')
    print("Antes:", [aluno.get_nome() for aluno in turma2.get_alunos()], [aluno.get_nome() for aluno in turma1.get_alunos()])
    curso1.remove_aluno(aluno3)
    aluno3.remove_curso(curso1)
    print("Depois:",[aluno.get_nome() for aluno in turma2.get_alunos()], [aluno.get_nome() for aluno in turma1.get_alunos()])


if __name__ == '__main__':
    
    main()