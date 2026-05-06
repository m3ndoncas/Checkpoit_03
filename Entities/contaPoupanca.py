from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numeroConta):
        super().__init__(numeroConta)

    def render_juros(self):
        taxa = 0.02
        self.__saldo += self.__saldo * taxa




if __name__ == '__main__':
    contaPoupanca = ContaPoupanca(14567)
    print("poupanca saldo", contaPoupanca.getSaldo())
    contaPoupanca.depositar('abc')
    print("poupanca saldo", contaPoupanca.getSaldo())