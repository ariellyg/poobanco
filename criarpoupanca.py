from conta import Conta
from contapoupanca import Contapoupanca
class Criarpoupanca:
    if __name__ == '__main__':
        conta= Conta('21.342-7')
        print (type(conta))
        conta = Contapoupanca('21.342-7')
        print(type(conta))

        conta.creditar(500.87)
        conta.debitar(45.00)
        print(conta.get_saldo())