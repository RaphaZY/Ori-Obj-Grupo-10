class Cliente:

    def __init__(self, nome=None, cpg=None, telefone=None ):
        self.__nome = nome
        self.__cpg = cpg
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome
    
    def get_cpg(self):
        return self.__cpg
    
    def get_telefone(self):
        return self.__telefone
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_cpg(self, cpg):
        self.__cpg = cpg

    def set_telefone(self, telefone):
        self.__telefone = telefone
    









