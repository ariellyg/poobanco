from contaabstrata import Contaabstrata

class Conta(Contaabstrata):
    def __init__(self, numero):
        super().__init__(numero)

    def debitar(self, valor):
        self._saldo -= valor





