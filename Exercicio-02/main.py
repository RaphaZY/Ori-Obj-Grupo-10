from model.professor import Professor
from model.aluno_ensino_medio import AlunoEnsinoMedio
from model.aluno_graduacao import AlunoGraduacao

def main():
    
    prof1 = Professor()
    prof1.set_nome("Dr. Carlos Silva")
    prof1.set_cpf("123.456.789-00")
    prof1.set_email("carlos@uft.edu")
    prof1.set_sexo("M")
    prof1.set_telefone("1234-5678")
    prof1.set_titulacao_maxima("Doutorado")
    prof1.set_matricula("P001")

    prof2 = Professor()
    prof2.set_nome("Ms. Ana Santos")
    prof2.set_cpf("321.654.789-74")
    prof2.set_email("anasantos@uft.edu")
    prof2.set_sexo("F")
    prof2.set_telefone("1234-8745")
    prof2.set_titulacao_maxima("Mestrado")
    prof2.set_matricula("P002")
    
    
    aluno_medio = AlunoEnsinoMedio()
    aluno_medio.set_nome("João Pereira")
    aluno_medio.set_cpf("987.654.321-00")
    aluno_medio.set_email("joao@aluno.edu")
    aluno_medio.set_sexo("M")
    aluno_medio.set_telefone("7845-5678")
    aluno_medio.set_matricula("MED123")
    aluno_medio.adicionar_nota(7.0)
    aluno_medio.adicionar_nota(5.0)  # Média = 6.0
    
    aluno_graduacao = AlunoGraduacao()
    aluno_graduacao.set_nome("Maria Oliveira")
    aluno_graduacao.set_cpf("784.654.457-74")
    aluno_graduacao.set_email("mariaoli@aluno.edu")
    aluno_graduacao.set_sexo("F")
    aluno_graduacao.set_telefone("7575-0124")
    aluno_graduacao.set_matricula("MED456")
    aluno_graduacao.adicionar_nota(8.0)
    aluno_graduacao.adicionar_nota(6.0)  # Média = 7.0
    
    aluno_graduacao2 = AlunoGraduacao()
    aluno_graduacao2.set_nome("Pedro Costa")
    aluno_graduacao2.set_cpf("105.784.154-20")
    aluno_graduacao2.set_email("pedrocos@aluno.edu")
    aluno_graduacao2.set_sexo("M")
    aluno_graduacao2.set_telefone("2425-8496")
    aluno_graduacao2.set_matricula("GRAD789")
    aluno_graduacao2.adicionar_nota(6.5)
    aluno_graduacao2.adicionar_nota(6.5)  # Média = 6.5
    
    # Testando as funcionalidades
    
    print("=== PROFESSORES ===")
    prof1.imprimir_dados()
    prof2.imprimir_dados()
    
    print("\n=== ALUNOS ===")
    aluno_medio.imprimir_dados()
    aluno_graduacao.imprimir_dados()
    aluno_graduacao2.imprimir_dados()
    
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


# Exemplo de uso e teste das classes
if __name__ == "__main__":
    main()