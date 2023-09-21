from contapoupanca import Contapoupanca
from contaespecial import Contaespecial
from contaabstrata import Contaabstrata

class Bancolista:
    def __init__(self):
        self.contas = []
        self.juros = 0.01

    def cadastrar(self, conta: Contaabstrata):
        self.contas.append(conta)

    def procurar_conta(self, numero):
        conta_buscada = None
        for conta in self.contas:
            if conta.get_numero() == numero:
                conta_buscada = conta

        if conta_buscada == None:
            return 'conta inexistente'
        else:
            return conta_buscada

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print('conta inexistente')

    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        if isinstance(conta, Contaespecial):
            conta.renderbonus()
        else:
            print('conta inexistente')

    def saldo(self, numero):
        return self.procurar_conta(numero).get_saldo()

    def transferir(self, origem, destino, valor):
        conta_origem = self.procurar_conta(origem.get_numero())
        conta_destino = self.procurar_conta(destino.get_numero())
        if conta_destino and conta_origem:
            if conta_origem.get_saldo() <= valor:
                print('saldo insuficiente')
            else:
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
                print('saldo realizado com sucesso')
        else:
            print('conta inexistente')


    def render_juros(self, numero):
        conta_analisada = self.procurar_conta(numero)
        if conta_analisada:
            if isinstance(conta_analisada, Contapoupanca):
                conta_analisada.render_juros(self.juros)
                print('operação realizada com sucesso')
            else:
                print('operação invalida')
        else:
            print('conta inexistente')

    def transferir(self, origem, destino, valor):
        conta_origem = self.procurar_conta(origem.get_numero())
        conta_destino = self.procurar_conta(destino.get_numero())
        if conta_destino and conta_origem:
            if conta_origem.get_saldo() <= valor:
                print('saldo insuficiente')
            else:
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
                print('saldo realizado com sucesso')
        else:
            print('conta inexistente')

    def render_juros(self, numero):
        conta_analisada = self.procurar_conta(numero)
        if conta_analisada:
            if isinstance(conta_analisada, Contapoupanca):
                conta_analisada.render_juros(self.juros)
                print('operação realizada com sucesso')
            else:
                print('operação invalida')
        else:
            print('conta inexistente')

    def renderbonus(self, numero):
        conta = self.procurar_conta(numero)
        conta.renderbonus()
