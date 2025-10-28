class Turma():
    def __init__(self, id=None, descricao=None, professor=None, alunos=None, disciplina=None, curso=None):
        self.__id = id
        self.__descricao = descricao
        self.__disciplina = disciplina or []
        self.__professor = professor or []
        self.__alunos = alunos or []
        self.__curso = curso

    def tem_aluno(self, aluno):
        return aluno in self.__alunos

    def get_id(self):
        return self.__id

    def get_descricao(self):
        return self.__descricao
    
    def get_professor(self):
        return self.__professor

    def get_alunos(self):
        return self.__alunos

    def get_disciplina(self):
        return self.__disciplina

    def add_aluno(self, aluno):
        self.__alunos.append(aluno)

    def set_id(self, id):
        self.__id = id

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_professor(self, professor):
        self.__professor = professor

    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina

    def remove_aluno(self, aluno):
        for a in self.__alunos:
            if a.get_id() == aluno.get_id():   
                self.__alunos.remove(a)
                return True
        return False
    
    def get_curso(self):
        return self.__curso
    
    def set_curso(self, curso):
        self.__curso = curso

    def imprimir_dados(self):
        print(f"ID: {self.get_id()}\nDescricao: {self.get_descricao()}\nProfessor: {self.get_professor()}\nAlunos: {self.get_alunos()}\nDisciplina: {self.get_disciplina()}")
