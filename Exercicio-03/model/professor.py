from model.pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self,id=None, nome=None, naturalidade=None, escolaridade=None, tipo_ensino=None):
        super().__init__(id, nome, naturalidade, escolaridade)
        self.__tipo_ensino = tipo_ensino

    def get_tipo_ensino(self):
        return self.__tipo_ensino
    
    def set_tipo_ensino(self, tipo_ensino):
        self.__tipo_ensino = tipo_ensino

    def imprimir_dados(self):
        super().imprimir_dados()
        print(
              f'|Tipo Ensino: {self.get_tipo_ensino()}\n'
              )