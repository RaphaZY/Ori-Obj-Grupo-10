class Curso():
    def __init__(self, nome=None, descricao=None, turmas=None):
        self.__nome = nome
        self.__descricao = descricao
        self.__turmas = turmas or []

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
    
    def add_turma(self, turma):
        self.__turmas.append(turma)

    def get_professores(self):
        return set([turma.get_professor() for turma in self.__turmas])

    def get_disciplinas(self):
        return set([turma.get_disciplina() for turma in self.__turmas])

    def get_alunos(self):
        alunos = []
        for turma in self.__turmas:
            alunos.extend(turma.get_alunos())
        return set(alunos)
    
   
    def remove_turma(self, turma):
        if turma in self.__turmas:
            self.__turmas.remove(turma)
            return True
        return False
    
    def remove_aluno(self, aluno):
        removido = False
        for turma in self.__turmas:
            if turma.remove_aluno(aluno):
                removido = True
        return removido


    def __str__(self):
        return f"Nome: {self.__nome}\nDescricao: {self.__descricao} \nTurmas: {[turma.get_descricao() for turma in self.__turmas]}"
