from .conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numeroConta, cliente):
        super().__init__(numeroConta, cliente)


    def sacar(self, valor):
        taxa = 2
        saque_total = valor + taxa

        if self.getSaldo() >= saque_total:
            super().sacar(saque_total)
        else:
            print("Saldo insuficiente")









if __name__ == '__main__':
    contaCorrente = ContaCorrente(12345)
    contaCorrente.depositar(500)
    print("deposito", contaCorrente.getSaldo())
    contaCorrente.sacar(150)
    print(contaCorrente.getSaldo())