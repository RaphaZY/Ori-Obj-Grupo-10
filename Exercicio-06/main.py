from model.pessoa import Pessoa

def main():
    h1 = Pessoa()
    h1.set_sexo("M")
    h1.set_peso(80)
    h1.set_altura(1.80)

    m1 = Pessoa()
    m1.set_sexo("F")
    m1.set_peso(65)
    m1.set_altura(1.65)

    h2 = Pessoa()
    h2.set_sexo("M")
    h2.set_peso(140)
    h2.set_altura(1.72)

    m2 = Pessoa()
    m2.set_sexo("F")
    m2.set_peso(96)
    m2.set_altura(1.79)

    print(h1.calcularImc())
    print(h2.calcularImc())
    print(m1.calcularImc())
    print(m2.calcularImc())


if __name__ == "__main__":
   main()