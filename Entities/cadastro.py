from .cliente import Cliente
from .contaCorrente import ContaCorrente
from .contaPoupanca import ContaPoupanca


def Cadastrar_cliente():
    nome = input("Nome do cliente: ")
    cpf = input("CPF: ")

    cliente1 = Cliente(nome, cpf)

    numero_conta = int(input("Número da conta: "))

    print("\nTipo de conta:")
    print("1 - Conta Corrente.")
    print("2 - Conta Poupança.")

    opcao = int(input("Qual tipo de conta deseja cadastrar?"))

    match opcao:
        case 1:
            conta = ContaCorrente(numero_conta, cliente1)
            print("Conta corrente criada com sucesso")
            return conta
        case 2:
            conta = ContaPoupanca(numero_conta, cliente1)
            print("Conta poupança criada com sucesso")
            return conta
        case _:
            print("Opção inválida.")
