from model.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self,id=None, nome=None, naturalidade=None, escolaridade=None, curso=None):
        super().__init__(id, nome, naturalidade, escolaridade)
        self.__curso = curso or []

    def get_curso(self):
        return self.__curso
    
    def add_curso(self, curso):
        self.__curso.append(curso)

    def imprimir_dados(self):
        super().imprimir_dados()
        print(f'|Curso: {self.get_curso()}\n')
