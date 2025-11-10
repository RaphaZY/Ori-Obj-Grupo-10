from model.pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome=None, cargo=None):
        super().__init__(nome)
        self.__cargo = cargo
        self.__ocorrencias = []
        self.__dependentes = []

    def get_cargo(self):
        return self.__cargo
    
    def get_ocorrencias(self):
        return self.__ocorrencias
    
    def get_dependentes(self):
        return self.__dependentes
    
    def set_cargo(self, cargo):
        self.__cargo = cargo

    def add_ocorrencia(self, ocorrencia):
        self.__ocorrencias.append(ocorrencia)

    def add_dependente(self, dependente):
        self.__dependentes.append(dependente)

    def adicionar_ocorrencia(self, ocorrencia):
        self.add_ocorrencia(ocorrencia)

    def adicionar_dependente(self, dependente):
        self.add_dependente(dependente)

    def calcular_salario(self, ano, mes):
        salario = self.get_cargo().get_salario_bruto()

        # Filtra ocorrências do mês/ano informados
        for o in self.get_ocorrencias():
            if o.get_data_ocorrencia().year == ano and o.get_data_ocorrencia().month == mes:
                salario += o.get_valor()

        # Acrescenta R$100 para cada dependente menor de 18
        for d in self.get_dependentes():
            if d.calcular_idade() < 18:
                salario += 100.0

        return salario

    def listar_dependentes(self):
        for d in self.get_dependentes():
            print(f"\nDependente: {d.get_nome()}")
            print(f"Data de nascimento: {d.get_data_nascimento().strftime('%d/%m/%Y')}")
            print(f"Idade: {d.calcular_idade()} anos")
            print(f"Próximo aniversário: {d.proximo_aniversario().strftime('%d/%m/%Y')}")
            print(f"Dias para o aniversário: {d.dias_para_aniversario()}")
            print(f"Cai em: {d.dia_semana_aniversario()}")

    def imprimir_dados(self):
        super().imprimir_dados()
        print(f"|Cargo: {self.get_cargo().get_nome()}\n")

    