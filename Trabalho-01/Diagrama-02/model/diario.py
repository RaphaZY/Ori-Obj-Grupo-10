from decimal import Decimal

class Diario:
    def __init__(self, v1=0, v2=0, v3=0, vf=0, faltas=0):
        self.__v1 = v1
        self.__v2 = v2
        self.__v3 = v3
        self.__vf = vf
        self.__faltas = faltas

    def media_final(self):
        return (self.__v1 + self.__v2 + self.__v3 + self.__vf) / 4

    def get_faltas(self):
        return self.__faltas
    
    def set_faltas(self, faltas):
        self.__faltas = faltas  

    def set_notas(self, notas):
        notas = notas.split(',')
        v1 = notas[0]
        v2 = notas[1]
        v3 = notas[2]
        vf = notas[3]
        self.__v1 = Decimal(v1)
        self.__v2 = Decimal(v2)
        self.__v3 = Decimal(v3)
        self.__vf = Decimal(vf)

