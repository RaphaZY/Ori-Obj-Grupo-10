from model.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, id, nome=None, cpf=None, data_nascimento=None, email=None, endereco=None, telefone=None, identidade=None, matricula=None, ano_inicio=None, semestre_inicio=None):
        super().__init__(id, nome, cpf, data_nascimento, email, endereco, telefone, identidade)
        self.__matricula = matricula
        self.__ano_inicio = ano_inicio
        self.__semestre_inicio = semestre_inicio
        self.__situacoes = []
        self.__diarios = []

    def add_situacao(self, situacao):
        self.__situacoes.append(situacao)

    def add_diario(self, diario):
        self.__diarios.append(diario)

    def get_matricula(self):
        return self.__matricula
    
    def get_ano_inicio(self):
        return self.__ano_inicio
    
    def get_semestre_inicio(self):
        return self.__semestre_inicio
    
    def get_situacoes(self):
        for situacao in self.__situacoes:
            return situacao.get_situacao()

    def get_situacoes_ano_semestre(self):
        for situacao in self.__situacoes:
            return situacao.get_ano_semestre()

    def get_diarios(self):
        for diario in self.__diarios:
            return diario.media_final()
        
    def get_diarios_faltas(self):
        for diario in self.__diarios:
            return diario.get_faltas()
    

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def set_ano_inicio(self, ano_inicio):
        self.__ano_inicio = ano_inicio

    def set_semestre_inicio(self, semestre_inicio):
        self.__semestre_inicio = semestre_inicio

    def imprimir_dados(self):
        super().imprimir_dados()
        print(f"|Matricula: {self.get_matricula()}\n"
              f"|Ano de Início: {self.get_ano_inicio()}\n"
              f"|Semestre de Início: {self.get_semestre_inicio()}\n"
              )
        return ''