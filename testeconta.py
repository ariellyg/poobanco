from conta import Conta
conta = Conta('31.345-x')
conta.creditar(20)
especial = Contaespecial('31.345-x')
conta.creditar(20)
conta = especial
conta.crditar(20)