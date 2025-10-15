from model.professor import Professor
from model.aluno import Aluno
from model.turma import Turma
from model.disciplina import Disciplina
from model.curso import Curso
from datetime import datetime

professor1 = Professor()
aluno1 = Aluno()
aluno2 = Aluno()
aluno3 = Aluno()
turma1 = Turma(1)
turma2 = Turma(2)
disciplina1 = Disciplina()
disciplina2 = Disciplina()
curso1 = Curso()


professor1.set_nome("Marcos")
professor1.set_cpf("123.456.789-00")
professor1.set_endereco("Rua 1")
data_nascimento_prof1 = "01/01/2000"
data_nascimento_prof1 = datetime.strptime(data_nascimento_prof1, "%d/%m/%Y")
professor1.set_data_nascimento(data_nascimento_prof1)
professor1.set_telefone("1234-5678")
professor1.set_email("marcos@example.com")
professor1.set_sexo("M")
professor1.set_matricula("122123")
professor1.set_salario(1618)

aluno1.set_nome("João")
aluno1.set_cpf("123.456.789-00")
aluno1.set_endereco("Rua 1")
data_nascimento_aluno1 = datetime.now().strftime("%d/%m/%Y")
aluno1.set_data_nascimento()
aluno1.set_telefone("1234-5678")
aluno1.set_email("joao@example.com")
aluno1.set_sexo("M")
aluno1.set_matricula("121213")
aluno1.set_ano_inicio(2021)

aluno2.set_nome("Pedro")
aluno2.set_cpf("987.150.789-00")
aluno2.set_endereco("Rua 3")
aluno2.set_data_nascimento("09/06/2003")
aluno2.set_telefone("1234-5678")
aluno2.set_email("pedro@example.com")
aluno2.set_sexo("M")
aluno2.set_matricula("129404")
aluno2.set_ano_inicio(2021)

aluno3.set_nome("Maria")
aluno3.set_cpf("145.865.789-88")
aluno3.set_endereco("Rua 5")
aluno3.set_data_nascimento("09/06/2001")
aluno3.set_telefone("1234-5678")
aluno3.set_email("maria@example.com")
aluno3.set_sexo("F")
aluno3.set_matricula("129404")
aluno3.set_ano_inicio(2020)


disciplina1.set_nome("Matemática")
disciplina2.set_nome("BD")

turma1.set_descricao("Turma 1")
turma1.set_professor(professor1.get_nome())
turma1.add_aluno(aluno1)
turma1.add_aluno(aluno2)
turma1.add_aluno(aluno3)
turma1.set_disciplina(disciplina1.get_nome())

turma2.set_descricao("Turma 2")
turma2.set_professor(professor1.get_nome())
turma2.add_aluno(aluno2)
turma2.add_aluno(aluno3)
turma2.set_disciplina(disciplina2.get_nome())

curso1.set_nome("Ciência da Computação")
curso1.set_descricao("Curso de Ciência da Computação")
curso1.add_turma(turma1)
curso1.add_turma(turma2)

professor1.add_turma(turma1)
professor1.add_turma(turma2)

aluno1.add_turma(turma1)

aluno2.add_turma(turma1)
aluno2.add_turma(turma2)

aluno3.add_turma(turma1)
aluno3.add_turma(turma2)

print('----------Dados-----------')
professor1.imprimir_dados()
print('----------------------')
aluno1.imprimir_dados()
print('----------------------')
aluno2.imprimir_dados()
print('----------------------')
turma1.imprimir_dados()
print('----------------------')
turma2.imprimir_dados()
print('----------------------')
print(curso1)
print('----------------------')

print('----------01------------')
print(turma1.get_professor())

print('----------02------------')
print(turma1.get_alunos())

print('----------03------------')
print(curso1.get_professores())

print('----------04------------')
print(curso1.get_alunos())

print('----------05------------')
print(curso1.get_professores())

print('----------06------------')
print(curso1.get_disciplinas())

print('----------07------------')
print(turma1.tem_aluno(aluno1))

print('----------08------------')
print(aluno1.get_nome() in curso1.get_alunos())

print('----------09------------')
print(turma1.get_id() in curso1.get_turmas())

print('----------10------------')
print("Antes:", turma1.get_alunos())
turma1.remove_aluno(aluno1)
print("Depois:", turma1.get_alunos())

print('----------11------------')
print("Antes:", curso1.get_turmas())
curso1.remove_turma(turma2)
print("Depois:", curso1.get_turmas())

print('----------12------------')
print("Antes:", turma2.get_alunos(), turma1.get_alunos())
curso1.remove_aluno(aluno2)
print("Depois:", turma2.get_alunos(), turma1.get_alunos())