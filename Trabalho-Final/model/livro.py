class Livro:
    def __init__(self, id=None, titulo=None, autor=None, descricao=None):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__descricao = descricao

    # --------- GETTERS ---------
    def get_id(self):
        return self.__id
    
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_descricao(self):
        return self.__descricao


    # --------- SETTERS ---------
    def set_id(self, id):
        self.__id = int(id)

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_descricao(self, descricao):
        self.__descricao = descricao
        

    # --------- STR ---------
    def __str__(self):
        return f"{self.__id} - {self.__titulo} ({self.__autor}) : {self.__descricao}"
