from datetime import datetime, timedelta, date

class Emprestimo:
    def __init__(self, id_emprestimo=None, id_cliente=None, id_livro=None, data_inicio=None, data_entrega=None):
        self.__id_emprestimo = int(id_emprestimo) if id_emprestimo else None
        self.__id_cliente = int(id_cliente) if id_cliente else None
        self.__id_livro = int(id_livro) if id_livro else None

        # 🔹 Se vier string, converte; se vier date, mantém
        if isinstance(data_inicio, str):
            self.__data_inicio = datetime.strptime(data_inicio.strip(), "%d-%m-%Y").date()
        elif isinstance(data_inicio, date):
            self.__data_inicio = data_inicio
        else:
            self.__data_inicio = date.today()

        # 🔹 Mesmo para data_entrega
        if isinstance(data_entrega, str):
            self.__data_entrega = datetime.strptime(data_entrega.strip(), "%d-%m-%Y").date()
        elif isinstance(data_entrega, date):
            self.__data_entrega = data_entrega
        else:
            # 15 dias depois da data de início
            self.__data_entrega = self.__data_inicio + timedelta(days=15)

    # --------- GETTERS ---------
    def get_id(self):
        return self.__id_emprestimo

    def get_id_cliente(self):
        return self.__id_cliente

    def get_id_livro(self):
        return self.__id_livro

    def get_data_inicio(self):
        return self.__data_inicio

    def get_data_entrega(self):
        return self.__data_entrega

    # --------- SETTERS ---------
    def set_id_emprestimo(self, id_emprestimo):
        self.__id_emprestimo = int(id_emprestimo)

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = int(id_cliente)

    def set_id_livro(self, id_livro):
        self.__id_livro = int(id_livro)

    def set_data_inicio(self, data_inicio):
        if isinstance(data_inicio, str):
            self.__data_inicio = datetime.strptime(data_inicio.strip(), "%d-%m-%Y").date()
        else:
            self.__data_inicio = data_inicio

    def set_data_entrega(self, data_entrega):
        if isinstance(data_entrega, str):
            self.__data_entrega = datetime.strptime(data_entrega.strip(), "%d-%m-%Y").date()
        else:
            self.__data_entrega = data_entrega

    # --------- FORMATAÇÃO PARA SALVAR ---------
    def to_string_line(self):
        return f"{self.__id_emprestimo};{self.__id_cliente};{self.__id_livro};{self.__data_inicio.strftime('%d-%m-%Y')};{self.__data_entrega.strftime('%d-%m-%Y')}\n"

    # --------- REPRESENTAÇÕES ---------
    def listar_admin(self):
        return (f"ID {self.__id_emprestimo} | Cliente {self.__id_cliente} | Livro {self.__id_livro} | "
                f"Início {self.__data_inicio.strftime('%d/%m/%Y')} | Entrega {self.__data_entrega.strftime('%d/%m/%Y')}")

    def __str__(self):
        return (f"ID {self.__id_emprestimo} | Livro {self.__id_livro} | "
                f"Início {self.__data_inicio.strftime('%d/%m/%Y')} | Entrega {self.__data_entrega.strftime('%d/%m/%Y')}")
