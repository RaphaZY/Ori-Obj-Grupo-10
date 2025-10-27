from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, naturalidade, escolaridade, curso=None):
        super().__init__(nome, naturalidade, escolaridade)
        self.curso = curso
