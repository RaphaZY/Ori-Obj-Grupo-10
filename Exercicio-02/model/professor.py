from model.pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome=None, cpf=None, email=None, telefone=None, sexo=None, titulacao_maxima=None, matricula=None):
        super().__init__(nome, cpf, email, telefone, sexo)
        self.__titulacao_maxima = titulacao_maxima
        self.__matricula = matricula
    
    def get_titulacao_maxima(self):
        return self.__titulacao_maxima
    
    def set_titulacao_maxima(self, titulacao_maxima):
        self.__titulacao_maxima = titulacao_maxima
    
    def get_matricula(self):
        return self.__matricula
    
    def set_matricula(self, matricula):
        self.__matricula = matricula

    def imprimir_dados(self):
        super().imprimir_dados()
        print(f'|Matricula: {self.get_matricula()}')
        print(f'|Titulacao Maxima: {self.get_titulacao_maxima()}\n')    