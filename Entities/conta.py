
class Conta:
    def __init__(self, numeroConta):
        self.numeroConta = numeroConta
        self.__saldo = 0.0

    def getSaldo(self):
        return self.__saldo

    def depositar(self, valor):
            if not isinstance(valor, (int, float)):
                print("Valor inválido")
                return

            if valor > 0:
                self.__saldo += valor


    def sacar(self, valor):
            if not isinstance(valor, (int, float)):
                print("Valor inválido")
                return

            if self.__saldo >= valor:
                self.__saldo -= valor
                return self.__saldo
            else:
                print("Saldo insuficiente")

