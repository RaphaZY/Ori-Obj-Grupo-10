class Usuario:
    def __init__(self, id=None, nome=None, tipo=None, login=None, senha=None):
        self.__id = id
        self.__nome = nome
        self.__tipo = tipo
        self.__login = login
        self.__senha = senha


    # --------- GETTERS ---------
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_tipo(self):
        return self.__tipo
    
    def get_login(self):
        return self.__login
    
    def get_senha(self):
        return self.__senha

    # --------- SETTERS ---------
    def set_id(self, id):
        self.__id = int(id)

    def set_nome(self, nome):
        self.__nome = nome

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def set_login(self, login):
        self.__login = login

    def set_senha(self, senha):
        self.__senha = senha

    
    # --------- VALIDAÇÃO DE LOGIN ---------
    def validar_login(self, login, senha):
        return self.__login == login and self.__senha == senha
    
    # --------- STR ---------
    def __str__(self):
        return f"| {self.__id} | {self.__nome} | {self.__login} | {self.__senha} | {self.__tipo} |"  
