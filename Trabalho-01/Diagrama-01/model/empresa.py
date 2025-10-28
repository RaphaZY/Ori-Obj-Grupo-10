class Empresa:
    def __init__(self, id=None, codigo=None, razao_social=None, endereco=None, cnpj=None):
        self.__id = id
        self.__codigo = codigo
        self.__razao_social = razao_social
        self.__endereco = endereco
        self.__cnpj = cnpj
        self.__notas = []

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def add_nota(self, nota):
        self.__notas.append(nota)

    def get_razao_social(self):
        return self.__razao_social

    def get_notas(self):
        return self.__notas
    
    def set_codigo(self, codigo):
        self.__codigo = codigo  

    def set_razao_social(self, razao_social):
        self.__razao_social = razao_social

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def set_cnpj(self, cnpj):
        self.__cnpj = cnpj
