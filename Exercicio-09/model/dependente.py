from datetime import datetime
from model.pessoa import Pessoa
from model.funcionario import Funcionario

class Dependente(Pessoa):
    def __init__(self, nome=None, data_nascimento=None):
        super().__init__(nome)
        self.__data_nascimento = data_nascimento

    def get_data_nascimento(self):
        return self.__data_nascimento
    
    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

    def calcular_idade(self):
        hoje = datetime.today()
        idade = hoje.year - self.get_data_nascimento().year
        if (hoje.month, hoje.day) < (self.get_data_nascimento().month, self.get_data_nascimento().day):
            idade -= 1
        return idade

    def proximo_aniversario(self):
        hoje = datetime.today()
        proximo = datetime(hoje.year, self.get_data_nascimento().month, self.get_data_nascimento().day)
        if proximo < hoje:
            proximo = datetime(hoje.year + 1, self.get_data_nascimento().month, self.get_data_nascimento().day)
        return proximo

    def dias_para_aniversario(self):
        hoje = datetime.today()
        return (self.proximo_aniversario() - hoje).days

    def dia_semana_aniversario(self):
        dias = ['Segunda-feira', 'Terça-feira', 'Quarta-feira',
                'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
        return dias[self.proximo_aniversario().weekday()]
    
    def imprimir_dados(self):
        super().imprimir_dados()
        print(f"|Data de Nascimento: {self.get_data_nascimento().strftime('%d/%m/%Y')}\n")
    
    