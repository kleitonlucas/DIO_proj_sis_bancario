menu = f'''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

msg_deposito_erro = f'''
Depósito não autorizado!

Valor inválido.
'''

msg_saque_invalido = f'''
Saque não autorizado!

Valor inválido.
'''

msg_saque_erro_maior_que_saldo = f'''
Saque não autorizado!

Valor de saque maior que o valor de saldo.
'''

msg_saque_erro_maior_que_limite = f'''
Saque não autorizado!

Valor de saque maior que o valor de limite.
'''

msg_atingiu_limite_de_saque = f'''
Saque não autorizado!

Número de saques máximo atingido.
'''

msg_retorno_menu = 'Retornando ao menu inicial...'

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        deposito = float(input("Valor a ser depositado: "))
        if deposito > 0:
            saldo += deposito
            extrato += f'- Depósito     R$ {deposito:.2f}\n'
        else:
            print(msg_deposito_erro)
    elif opcao == 's':
        saque = float(input("Valor de saque: "))
        saque_maior_que_saldo = saque > saldo
        saque_maior_que_limite = saque > limite
        limite_de_saques_atingido = numero_saques >= LIMITE_SAQUES

        if saque_maior_que_saldo:
            print(msg_saque_erro_maior_que_saldo)
        elif saque_maior_que_limite:
            print(msg_saque_erro_maior_que_limite)
        elif limite_de_saques_atingido:
            print(msg_atingiu_limite_de_saque)
        elif saque > 0:
            saldo -= saque
            extrato += f'- Saque        R$ {saque:.2f}\n'
            numero_saques += 1
        else:
            print(msg_saque_invalido)
    elif opcao == 'e':
        print(" Extrato ".center(30, '_'))
        print(extrato)
        print(f"\n- Saldo        R$ {saldo:.2f}")
        print("".center(30, '_'))
    elif opcao == 'q':
        print("Saindo...")
        break
    else:
        print("Operação inválida! Por favor, selecione uma opção desejada.")
