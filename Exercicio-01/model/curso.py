class Curso():
    def __init__(self, nome=None, descricao=None, turmas=None, alunos=None):
        self.__nome = nome
        self.__descricao = descricao
        self.__turmas = turmas or []
        self.__alunos = alunos or []

    def get_nome(self):
        return self.__nome
    
    def get_descricao(self):
        return self.__descricao
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_turmas(self):
        return [turma.get_id() for turma in self.__turmas]
    
    def get_turma(self, id):
        for turma in self.__turmas:
            if turma.get_id() == id:
                return turma
    
    def add_turma(self, turma):
        self.__turmas.append(turma)

    def add_aluno(self, aluno):
        self.__alunos.append(aluno)

    def get_professores(self):
        return set([turma.get_professor() for turma in self.__turmas])

    def get_disciplinas(self):
        return [turma.get_disciplina() for turma in self.__turmas]

    def get_alunos(self):
        return [aluno.get_nome() for aluno in self.__alunos]
    
    def verifica_aluno(self, aluno):
        return aluno in self.__alunos
    
    def get_alunos_turma(self, turma):
        return turma.get_alunos()
   
    def remove_turma(self, turma):
        if turma in self.__turmas:
            self.__turmas.remove(turma)
            return True
        return False
    
    def remove_aluno(self, aluno):
        if aluno in self.__alunos:
            self.__alunos.remove(aluno)

        for turma in self.__turmas:
            turma.remove_aluno(aluno)

        return True


    def __str__(self):
        return f"Nome: {self.__nome}\nDescricao: {self.__descricao} \nTurmas: {[turma.get_descricao() for turma in self.__turmas]}"
