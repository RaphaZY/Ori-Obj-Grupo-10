from model.funcionario import Funcionario

def main():
    funcionario1 = Funcionario()
    funcionario1.set_nome("Gabriel M.")
    funcionario1.set_salario_bruto(1800)
    funcionario1.set_total_acrescimos(100)
    funcionario1.set_total_descontos(50)

    print(f"Nome: {funcionario1.get_nome()}")
    print(f"Salário Bruto: {funcionario1.get_salario_bruto()}")
    print(f"Salário Liquido: {funcionario1.calcular_salario_liquido()}")


if __name__ == '__main__':
    
    main()
  