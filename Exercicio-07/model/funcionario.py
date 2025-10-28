class Funcionario:
    
    def __init__(self, id=None, nome=None, salario_bruto=None, total_acrescimos=0, total_descontos=0):
        self.__id = id
        self.__nome = nome
        self.__salario_bruto = salario_bruto
        self.__total_acrescimos = total_acrescimos
        self.__total_descontos = total_descontos
    

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome
    
    def get_salario_bruto(self):
        return self.__salario_bruto
    
    def get_total_acrescimos(self):
        return self.__total_acrescimos
    
    def get_total_descontos(self):
        return self.__total_descontos
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_salario_bruto(self, salario_bruto):
        self.__salario_bruto = salario_bruto
    
    def set_total_acrescimos(self, total_acrescimos):
        self.__total_acrescimos = total_acrescimos
    
    def set_total_descontos(self, total_descontos):
        self.__total_descontos = total_descontos
    
    def calcular_salario_liquido(self):
        salario_liquido = self.__salario_bruto + self.__total_acrescimos - self.__total_descontos
        return salario_liquido