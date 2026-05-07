from Entities.cadastro import Cadastrar_cliente
from Entities.contaPoupanca import ContaPoupanca


def menu():
    print("=" * 30)
    print("      MENU BANCÁRIO")
    print("=" * 30)
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")
    print("=" * 30)



def main():
    conta = Cadastrar_cliente()

    while True:
        menu()

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                try:
                    valor = float(input("Valor do depósito: R$ "))
                    conta.depositar(valor)
                    print("Depósito realizado com sucesso")

                except ValueError:
                    print("Digite apenas números")

            case "2":
                try:
                    valor = float(input("Valor do saque: R$ "))
                    conta.sacar(valor)

                except ValueError:
                    print("Digite apenas números")

            case "3":
                print(f"\nSaldo atual: R$ {conta.getSaldo():.2f}")

            case "4":
                print("Saindo do sistema...")
                break

            case _:
                print("Opção inválida")



if __name__ == "__main__":
    main()