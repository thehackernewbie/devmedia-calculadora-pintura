class Comodo:
    __largura: float
    __profundidade: float
    __altura: float

    def __init__(self, largura, profundidade):
        self.largura = float(largura)
        self.profundidade = float(profundidade)
        self.altura = 2.9

    @property
    def largura(self):
        return self.__largura

    @property
    def profundiade(self):
        return self.__profundidade

    @property
    def altura(self):
        return self.__altura
