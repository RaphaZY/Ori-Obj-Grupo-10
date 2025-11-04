from model.aluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__(self, nome=None, cpf=None, email=None, telefone=None, sexo=None, matricula=None, notas=None):
        super().__init__(nome, cpf, email, telefone, sexo, matricula, notas)
    
    def foi_aprovado(self):
        media = self.calcular_media()
        return media >= 7
