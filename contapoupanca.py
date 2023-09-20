from conta import Conta

class Contapoupanca(Conta):

    def __init__(self, numero):
        super().__init__(numero)

    def render_juros(self, taxa):
        self.creditar(self.get_saldo() * taxa)