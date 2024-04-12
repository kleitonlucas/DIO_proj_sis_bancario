import textwrap


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

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    saque_maior_que_saldo = valor > saldo
    saque_maior_que_limite = valor > limite
    limite_de_saques_atingido = numero_saques >= limite_saques

    if saque_maior_que_saldo:
        print('-- Saque não autorizado! Valor de saque maior que o valor de saldo. --')
    elif saque_maior_que_limite:
        print('-- Saque não autorizado! Valor de saque maior que o valor de limite. --')
    elif limite_de_saques_atingido:
        print('-- Saque não autorizado! Número de saques máximo atingido. --')
    elif valor > 0:
        saldo -= valor
        extrato += f'- Saque        R$ {valor:.2f}\n'
        numero_saques += 1
        print('-- Saque realizado com sucesso. --')
    else:
        print('-- Saque não autorizado! Valor inválido. --')

    return saldo, extrato

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'- Depósito     R$ {valor:.2f}\n'
        print('-- Depósito realizado com sucesso! --')
    else:
        print('-- Depósito não autorizado! Valor inválido. --')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(' Extrato '.center(30, '_'))
    print(extrato)
    print(f'\n- Saldo        R$ {saldo:.2f}')
    print(''.center(30, '_'))

def criar_usuario(usuarios):
    msg_orientacao = '''ORIENTAÇÃO:
        \r- Data de nascimento de seguir o padrão: dia/mês/ano
        \r- Endereço deve seguir o padrão: logradouro, numero - bairro - cidade/estado'''
    print(' Cadastro de Usuários '.center(30, '-'))
    print(textwrap.dedent(msg_orientacao))
    cpf = input('CPF: ')
    usuario_encontrado = filtrar_usuario_por_cpf(cpf, usuarios)
    if usuario_encontrado:
        print('-- CPF já cadastrado! --')
        return
    nome = input('Nome: ')
    data_de_nascimento = input('Data de nascimento: ')
    endereço = input('Endereço: ')

    novo_usuario = {'nome': nome, 'data_de_nascimento': data_de_nascimento, 'cpf': cpf, 'endereco': endereço}

    usuarios.append(novo_usuario)
    print('-- Usuário cadastrado! --')

def filtrar_usuario_por_cpf(cpf, usuarios):
    usuario_encontrado = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuario_encontrado[0] if usuario_encontrado else None

def criar_conta_corrente(agencia, contas, usuarios):
    print(' Cadastro de Contas '.center(30, '-'))
    cpf = input('CPF: ')
    usuario = filtrar_usuario_por_cpf(cpf, usuarios)

    if usuario:
        numero_conta = gerar_numero_conta(contas)
        nova_conta = {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
        contas.append(nova_conta)
        print('-- Conta criada com sucesso. --')
    else:
        print('-- Usuário não encontrado, não é possível continuar. --')

def gerar_numero_conta(contas):
    if not contas:
        return 1
    else:
        return contas[-1]['numero_conta'] + 1

def listar_usuarios(usuarios):
    for usuario in usuarios:
        dados_usuario = f'''\
            Nome:\t\t{usuario['nome']}
            Data de nascimento:\t{usuario['data_de_nascimento']}
            CPF:\t\t{usuario['cpf']}
            Endereço:\t\t{usuario['endereco']}
        '''
        print(' Usuários '.center(30, '_'))
        print(dados_usuario)

def listar_contas(contas):
    for conta in contas:
        dados_conta = f'''\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('-' * 30)
        print(textwrap.dedent(dados_conta))

def main():
    LIMITE_SAQUES = 3
    NUMERO_AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input("Valor a ser depositado: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == 's':
            valor = float(input("Valor de saque: "))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == 'nc':
            criar_conta_corrente(NUMERO_AGENCIA, contas, usuarios)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'nu':
            criar_usuario(usuarios)
        elif opcao == 'lu':
            listar_usuarios(usuarios)
        elif opcao == 'q':
            print("Saindo...")
            break
        else:
            print('-- Operação inválida! Por favor, selecione uma opção desejada. --')

main()