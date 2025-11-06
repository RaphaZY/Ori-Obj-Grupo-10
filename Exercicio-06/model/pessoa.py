
class Pessoa():
    def __init__(self, sexo=None, peso=None, altura=None):
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura


    def get_sexo(self):
        return self.__sexo

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def calcularImc(self):
        if self.get_sexo() == 'M':
            imc = self.get_peso() / (self.get_altura() ** 2)
            if imc < 20.7:
                return f"IMC = {imc:.2f} | Condição: abaixo do peso"
            elif 20.7 <= imc < 26.4:
                return f"IMC = {imc:.2f} | Condição: no peso normal"
            elif 26.4 <= imc < 27.8:
                return f"IMC = {imc:.2f} | Condição: marginalmente acima do peso"
            elif 27.8 <= imc < 31.1:
                return f"IMC = {imc:.2f} | Condição: acima do peso ideal"
            else:
                return f"IMC = {imc:.2f} | Condição: obeso"
        else:
            imc = self.get_peso() / (self.get_altura() ** 2)
            if imc < 19.1:
                return f"IMC = {imc:.2f} | Condição: abaixo do peso"
            elif 19.1 <= imc < 25.8:
                return f"IMC = {imc:.2f} | Condição: no peso normal"
            elif 25.8 <= imc < 27.3:
                return f"IMC = {imc:.2f} | Condição: marginalmente acima do peso"
            elif 27.3 <= imc < 32.3:
                return f"IMC = {imc:.2f} | Condição: acima do peso ideal"
            else:
                return f"IMC = {imc:.2f} | Condição: obeso"
            
