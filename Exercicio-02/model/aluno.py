from model.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome=None, cpf=None, email=None, telefone=None, sexo=None, matricula=None, notas=None):
        super().__init__(nome, cpf, email, telefone, sexo)
        self.__matricula = matricula
        self.__notas = notas or []

    def get_notas(self):
        return self.__notas
    
    def get_matricula(self):
        return self.__matricula
    
    def set_matricula(self, matricula):
        self.__matricula = matricula


    def adicionar_nota(self, nota):
        self.__notas.append(nota)
    
    def calcular_media(self):
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)
    
    def foi_aprovado(self):
        # Método abstrato - será implementado nas subclasses
        raise NotImplementedError("Método deve ser implementado na subclasse")
    
    def get_info_completa(self):
        status = "Aprovado" if self.foi_aprovado() else "Reprovado"
        return f"Aluno: {self.get_nome()}, Matrícula: {self.get_matricula()}, Media: {self.calcular_media()}, Status: {status}"
    
    def imprimir_dados(self):
        super().imprimir_dados()
        print(f'|Matricula: {self.get_matricula()}\n')
     