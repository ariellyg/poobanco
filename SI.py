class SIException:

    def __init__(self, saldo,numero, message='saldo insuficiente'):
        self.saldo = saldo
        self.numero = numero
        self.message = message
        super().__init__(self.message)

    def numeroConta(self):
        self.numero

    def saldoConta(self):
        self.saldo