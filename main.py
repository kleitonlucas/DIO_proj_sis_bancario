import textwrap

from contacorrente import ContaCorrente
from deposito import Deposito
from pessoafisica import PessoaFisica
from saque import Saque


def menu():
    menu = '''\n
    _____________ MENU _____________
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [lu]\tListar Usuários
    [q]\tSair
    => '''
    return input(textwrap.dedent(menu))

def depositar(clientes):
    cpf = input('CPF do cliente: ')
    cliente = filtrar_cliente_cpf(cpf, clientes)

    if cliente:
        valor = float(input('Valor de depósito: '))
        transacao = Deposito(valor)

        conta = filtrar_conta_cliente(cliente)
        if conta:
            cliente.realizar_transacao(conta, transacao)
        else: 
            return
    else:
        print('-- Cliente não cadastrado! --')

def sacar(clientes):
    cpf = input('CPF do cliente: ')
    cliente = filtrar_cliente_cpf(cpf, clientes)

    if cliente:
        valor = float(input('Valor de saque: '))
        transacao = Saque(valor)

        conta = filtrar_conta_cliente(cliente)
        if conta:
            cliente.realizar_transacao(conta, transacao)
        else: 
            return
    else:
        print('-- Cliente não cadastrado! --')

def exibir_extrato(clientes):
    cpf = input('CPF do cliente: ')
    cliente = filtrar_cliente_cpf(cpf, clientes)

    if cliente:
        conta = filtrar_conta_cliente(cliente)
        
        if conta:
            print(' Extrato '.center(30, '_'))
            transacoes = conta.historico.transacoes
            extrato = ''

            if transacoes:
                for transacao in transacoes:
                    extrato += f'''\n{transacao["tipo"]}:\n\tR$ {transacao["valor"]:.2f}'''
            else:
                extrato = 'Não foram realizadas movimentações.'
            print(extrato)
            print(f'\nSaldo:\n\tR$ {conta.saldo:.2f}')
            print(''.center(30, '_'))
        else: 
            return
    else:
        print('-- Cliente não cadastrado! --')

def criar_conta_corrente(numero_conta, clientes, contas):
    cpf = input('CPF do cliente: ')
    cliente = filtrar_cliente_cpf(cpf, clientes)

    if cliente:
        conta = ContaCorrente.nova_conta(cliente, numero_conta)
        contas.append(conta)
        cliente.contas.append(conta)
        print('-- Conta criada com sucesso! --')
    else:
        print('-- Cliente não cadastrado! Conta não criada. --')

def criar_cliente(clientes):
    cpf = input('CPF do cliente: ')
    cliente = filtrar_cliente_cpf(cpf, clientes)

    if not cliente:
        nome = input('Nome: ')
        data_nascimento = input('Data de Nascimento (dd/mm/aaaa): ')
        endereco = input('Endereço (logradouro, nro - bairro - cidade/estado): ')

        cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)

        clientes.append(cliente)
        print('-- Cliente cadastrado com sucesso! --')
    else:
        print('-- CPF já cadastrado! --')

def filtrar_cliente_cpf(cpf, clientes):
    cliente = [cliente for cliente in clientes 
                if cliente.cpf == cpf]
    return cliente[0] if cliente else None

def filtrar_conta_cliente(cliente):
    if cliente.contas:
        #Ainda não é possível escolher a conta
        return cliente.contas[0]
    else:
        print('-- Cliente não possui conta! --')
        return None

def listar_contas(contas):
    for conta in contas:
        print('-' * 30)
        print(textwrap.dedent(str(conta)))

def listar_clientes(clientes):
    for cliente in clientes:
        print('-' * 30)
        print(textwrap.dedent(str(cliente)))

def main():
    clientes = []
    contas = []
    
    while True:
        opcao = menu()

        if opcao == 'd':
            depositar(clientes)
        elif opcao == 's':
            sacar(clientes)
        elif opcao == 'e':
            exibir_extrato(clientes)
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            criar_conta_corrente(numero_conta, clientes, contas)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'nu':
            criar_cliente(clientes)
        elif opcao == 'lu':
            listar_clientes(clientes)
        elif opcao == 'q':
            print("Saindo...")
            break
        else:
            print('-- Operação inválida! Por favor, selecione uma opção desejada. --')

# main()

#TESTE
clientes = []
contas = []

criar_cliente(clientes)
criar_conta_corrente(len(contas) + 1, clientes, contas)
listar_clientes(clientes)
listar_contas(contas)
depositar(clientes)
exibir_extrato(clientes)
sacar(clientes)
sacar(clientes)
sacar(clientes)
exibir_extrato(clientes)
sacar(clientes)
exibir_extrato(clientes)