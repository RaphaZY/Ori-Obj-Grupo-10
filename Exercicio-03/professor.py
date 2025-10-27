from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, naturalidade, escolaridade, tipo_ensino=None):
        super().__init__(nome, naturalidade, escolaridade)
        self.tipo_ensino = tipo_ensino
