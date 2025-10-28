from model.pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, id=None, nome=None, cpf=None, data_nascimento=None, email=None, endereco=None, telefone=None, identidade=None, matricula=None, titulacao_maxima=None):
        super().__init__(id, nome, cpf, data_nascimento, email, endereco, telefone, identidade)
        self.__matricula = matricula
        self.__titulacao_maxima = titulacao_maxima
        self.__cursos = []

    def add_curso(self, curso):
        self.__cursos.append(curso)

    def get_matricula(self):
        return self.__matricula

    def get_titulacao_maxima(self):
        return self.__titulacao_maxima
    
    def set_matricula(self, matricula):
        self.__matricula = matricula    

    def set_titulacao_maxima(self, titulacao_maxima):
        self.__titulacao_maxima = titulacao_maxima

    def imprimir_dados(self):
        super().imprimir_dados()
        print(f"|Matricula: {self.get_matricula()}\n"
              f"|Titulação Máxima: {self.get_titulacao_maxima()}\n"
              )
        return ''