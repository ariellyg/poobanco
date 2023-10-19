class CIExcepition(Exception):
    def __init__(self, numero, message='conta inesxistente'):
        self.numero = numero
        self.message = message
        super().__init__(self.message)

    def numeroConta(self):
        return self.numero
