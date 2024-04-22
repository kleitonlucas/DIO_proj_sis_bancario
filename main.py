import textwrap

from contacorrente import ContaCorrente
from contaiterador import IteradorContas
from deposito import Deposito
from log import log_transacao
from pessoafisica import PessoaFisica
from saque import Saque


def menu():
    menu = """\n
    _____________ MENU _____________
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [lu]\tListar Usuários
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


@log_transacao
def depositar(clientes):
    cpf = input("CPF do cliente: ")
    cliente = filtrar_cliente_cpf(cpf, clientes)

    if cliente:
        valor = float(input("Valor de depósito: "))
        transacao = Deposito(valor)

        conta = filtrar_conta_cliente(cliente)
        if conta:
            cliente.realizar_transacao(conta, transacao)
        else:
            return
    else:
        print("-- Cliente não cadastrado! --")


@log_transacao
def sacar(clientes):
    cpf = input("CPF do cliente: ")
    cliente = filtrar_cliente_cpf(cpf, clientes)

    if cliente:
        valor = float(input("Valor de saque: "))
        transacao = Saque(valor)

        conta = filtrar_conta_cliente(cliente)
        if conta:
            cliente.realizar_transacao(conta, transacao)
        else:
            return
    else:
        print("-- Cliente não cadastrado! --")


@log_transacao
def exibir_extrato(clientes):
    cpf = input("CPF do cliente: ")
    cliente = filtrar_cliente_cpf(cpf, clientes)

    if cliente:
        conta = filtrar_conta_cliente(cliente)

        if conta:
            print(" Extrato ".center(30, "_"))
            extrato = ""
            tem_transacao = False

            for transacao in conta.historico.gerar_relatorio():
                tem_transacao = True
                extrato += f'\n{transacao["data"]}\n{transacao["tipo"]}:\n\tR$ {transacao["valor"]:.2f}\n'
            if not tem_transacao:
                extrato = "Não foram realizadas movimentações."

            print(extrato)
            print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
            print("".center(30, "_"))
        else:
            return
    else:
        print("-- Cliente não cadastrado! --")


@log_transacao
def criar_conta_corrente(numero_conta, clientes, contas):
    cpf = input("CPF do cliente: ")
    cliente = filtrar_cliente_cpf(cpf, clientes)

    if cliente:
        conta = ContaCorrente.nova_conta(cliente, numero_conta)
        contas.append(conta)
        cliente.contas.append(conta)
        print("-- Conta criada com sucesso! --")
    else:
        print("-- Cliente não cadastrado! Conta não criada. --")


@log_transacao
def criar_cliente(clientes):
    cpf = input("CPF do cliente: ")
    cliente = filtrar_cliente_cpf(cpf, clientes)

    if not cliente:
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
        endereco = input("Endereço (logradouro, nro - bairro - cidade/estado): ")

        cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)

        clientes.append(cliente)
        print("-- Cliente cadastrado com sucesso! --")
    else:
        print("-- CPF já cadastrado! --")


def filtrar_cliente_cpf(cpf, clientes):
    cliente = [cliente for cliente in clientes if cliente.cpf == cpf]
    return cliente[0] if cliente else None


def filtrar_conta_cliente(cliente):
    if cliente.contas:
        # Ainda não é possível escolher a conta
        return cliente.contas[0]
    else:
        print("-- Cliente não possui conta! --")
        return None


def listar_contas(contas):
    for conta in IteradorContas(contas):
        print("-" * 30)
        print(textwrap.dedent(str(conta)))


def listar_clientes(clientes):
    for cliente in clientes:
        print("-" * 30)
        print(textwrap.dedent(str(cliente)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta_corrente(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "lu":
            listar_clientes(clientes)
        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print("-- Operação inválida! Por favor, selecione uma opção desejada. --")


main()