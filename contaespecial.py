from conta import Conta

class Contaespecial(Conta):
    def __init__(self, numero):
        super().___init__(numero)
        self.__bonus = 0

    def renderbonus(self):
        super().creditar(self.__bonus)
        self.__bonus = 0

    def creditar(self, valor):
        self.__bonus = self.__bonus + (0.01 * valor)
        super().creditar(valor)
