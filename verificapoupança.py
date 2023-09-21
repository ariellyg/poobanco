from conta import Conta
from contapoupanca import Contapoupanca

class Verificapoupanca:
    if __name__ == '__main__':
        opcao = int(input('escolha: [1] Conta e [2] Poupança:'))
        if opcao == 1:
            conta = Conta('21.342-7')
        else:
            conta = Contapoupanca('21.342-7')
        conta.creditar(500.87)
        conta.debitar(45.00)

        if isinstance(conta, Contapoupanca):
            conta.render_juros(0.1)
            print(f'saldo com juros: {conta.get_saldo()}')

