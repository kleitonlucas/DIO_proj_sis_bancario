from conta import Conta
from saque import Saque


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [
                transacao for transacao in self.historico.transacoes
                    if transacao['tipo'] == Saque.__name__
            ]
        )

        valor_de_saque_maior_que_o_limite = valor > self.limite
        atingiu_o_limite_de_saques = numero_saques >= self.limite_saques
        # valor_de_saque_maior_que_saldo = valor > self.saldo
        # valor_de_saque_valido = valor > 0

        if valor_de_saque_maior_que_o_limite:
            print('-- Saque não autorizado! Valor de saque maior que o limite. --')
        elif atingiu_o_limite_de_saques:
            print('-- Saque não autorizado! Número de saques máximo atingido. --')
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f'''\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        '''