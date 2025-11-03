class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome


class Professor(Pessoa):
    def __init__(self, nome, titulacao_maxima):
        super().__init__(nome)
        self.titulacao_maxima = titulacao_maxima
    
    def get_titulacao_maxima(self):
        return self.titulacao_maxima
    
    def __str__(self):
        return f"Professor: {self.nome}, Titulação: {self.titulacao_maxima}"


class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula
        self.notas = []
    
    def adicionar_nota(self, nota):
        self.notas.append(nota)
    
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def foi_aprovado(self):
        # Método abstrato - será implementado nas subclasses
        raise NotImplementedError("Método deve ser implementado na subclasse")
    
    def get_info_completa(self):
        status = "Aprovado" if self.foi_aprovado() else "Reprovado"
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}, Status: {status}"
    
    def get_matricula(self):
        return self.matricula


class AlunoEnsinoMedio(Aluno):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
    
    def foi_aprovado(self):
        media = self.calcular_media()
        return media >= 6


class AlunoGraduacao(Aluno):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
    
    def foi_aprovado(self):
        media = self.calcular_media()
        return media >= 7


# Exemplo de uso e teste das classes
if __name__ == "__main__":
    # Criando professores
    prof1 = Professor("Dr. Carlos Silva", "Doutorado")
    prof2 = Professor("Ms. Ana Santos", "Mestrado")
    
    # Criando alunos
    aluno_medio = AlunoEnsinoMedio("João Pereira", "MED123")
    aluno_medio.adicionar_nota(7.0)
    aluno_medio.adicionar_nota(5.0)  # Média = 6.0
    
    aluno_graduacao = AlunoGraduacao("Maria Oliveira", "GRAD456")
    aluno_graduacao.adicionar_nota(8.0)
    aluno_graduacao.adicionar_nota(6.0)  # Média = 7.0
    
    aluno_graduacao2 = AlunoGraduacao("Pedro Costa", "GRAD789")
    aluno_graduacao2.adicionar_nota(6.5)
    aluno_graduacao2.adicionar_nota(6.5)  # Média = 6.5
    
    # Testando as funcionalidades
    
    print("=== PROFESSORES ===")
    print(prof1)
    print(prof2)
    
    print("\n=== ALUNOS - INFORMAÇÕES COMPLETAS ===")
    print(aluno_medio.get_info_completa())
    print(aluno_graduacao.get_info_completa())
    print(aluno_graduacao2.get_info_completa())
    
    print("\n=== VERIFICAÇÃO DE APROVAÇÃO ===")
    print(f"{aluno_medio.get_nome()} foi aprovado? {aluno_medio.foi_aprovado()}")
    print(f"{aluno_graduacao.get_nome()} foi aprovado? {aluno_graduacao.foi_aprovado()}")
    print(f"{aluno_graduacao2.get_nome()} foi aprovado? {aluno_graduacao2.foi_aprovado()}")
    
    print("\n=== TITULAÇÃO DOS PROFESSORES ===")
    print(f"{prof1.get_nome()}: {prof1.get_titulacao_maxima()}")
    print(f"{prof2.get_nome()}: {prof2.get_titulacao_maxima()}")