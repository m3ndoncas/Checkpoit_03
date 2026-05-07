from .conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numeroConta, cliente):
        super().__init__(numeroConta, cliente)

    def render_juros(self):
        taxa = 0.0101
        rendimento = self.getSaldo() * taxa
        self.depositar(rendimento)



if __name__ == '__main__':
    contaPoupanca = ContaPoupanca(14567)
