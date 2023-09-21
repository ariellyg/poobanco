from conta import Conta
from contapoupanca import Contapoupanca
from contaabstrata import Contaabstrata
class Banco:
    def __init__(self, numero):
       self.contas= [None] * 100
       self.indice = 0
       self.juros = 0.01

    def cadastrar(self, conta: Conta):
       self.contas[self.indice] = conta
       self.indice += 1

    def procurar_conta(self, numero):
        i= 0
        achou= False
        while achou is False and i < self.indice:
            if self.contas[i].get_numero() == numero:
                achou = True
            else:
                i += 1

        if achou is True:
            return self.contas[i]
        else:
            return None

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print('conta inexistente')

    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            if conta.get_saldo() < valor:
                print('o valor excedeu seu saldo')
            else:
                conta.creditar(valor)
        else:
            print('conta inexistente')

    def saldo(self, numero):
        return self.procurar_conta(numero).get_saldo()

    def transferir(self, origem, destino, valor):
        conta_origem = self.procurar_conta(origem.get_numero())
        conta_destino = self.procurar_conta(destino.get_numero())
        if conta_destino and conta_origem:
            if conta_origem.get_saldo() >= valor:
                print('saldo insuficiente')
            else:
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
        else:
            print('conta inexistente')

    def render_juros(self, numero):
        conta_analisada = self.procurar_conta(numero)
        if conta_analisada:
            if isinstance(conta_analisada, Contapoupanca):
                conta_analisada.render_juros(self.juros)
            else:
                print('operação invalida')
        else:
            print('conta inexistente')





