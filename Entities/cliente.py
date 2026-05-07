import re


class Cliente:
    def __init__(self, nome, cpf):
        # cpf True -> (False) ñ entra no if/ cpf False -> (True) entra no if
        if not self.validar_cpf(cpf):
            # interrompe o programa
            raise ValueError("CPF inválido")

        self.nome = nome
        self.__cpf = cpf

    @staticmethod
    def validar_cpf(cpf):
        padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$'

        if not re.match(padrao, cpf):
            return False

        cpf = cpf.replace('.', '').replace('-', '')

        if cpf == cpf[0] * 11:
            return False

        return True



if __name__ == "__main__":
    cliente = Cliente("Vitor", "12345678910")
