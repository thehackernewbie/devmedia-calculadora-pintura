class Calculadora:

    __area_paredes: float
    __area_teto: float

    def calcular_area_paredes(self, largura, profundidade, altura):
        self.__area_paredes = 2 * (largura + profundidade) * altura
        return self.__area_paredes

    def calcular_area_teto(self, largura, profundidade):
        self.__area_teto = largura * profundidade
        return self.__area_teto

    def calcular_litragem(self):
        return (self.__area_paredes + self.__area_teto) / 10
