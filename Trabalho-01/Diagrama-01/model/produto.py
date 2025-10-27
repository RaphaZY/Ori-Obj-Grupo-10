class Produto:
    def __init__(self, id, codigo=None, descricao=None):
        self.__id = id
        self.__codigo = codigo
        self.__descricao = descricao
        self.__itens = []

    def add_item(self, item):
        self.__itens.append(item)

    def get_descricao(self):
        return self.__descricao
    
    def set_codigo(self, codigo):
        self.__codigo = codigo
    
    def set_descricao(self, descricao):
        self.__descricao = descricao
