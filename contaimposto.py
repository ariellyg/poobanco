from contaabstrata import Contaabstrata
class Contaimposto(Contaabstrata):
    def __init__(self,numero):
        super().__init__(numero)

    def debitar(self,valor):
        self._saldo = self._saldo - (valor + (valor * 0.001))