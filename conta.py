from historico import Historico


class Conta:
    def __init__(self, numero, cliente):
        self._agencia = '0001'
        self._saldo = 0
        self._numero = numero
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        valor_de_saque_maior_que_saldo = valor > self.saldo
        valor_de_saque_valido = valor > 0

        if valor_de_saque_maior_que_saldo:
            print('-- Saque não autorizado! Valor de saque maior que o saldo. --')
        elif valor_de_saque_valido:
            self._saldo -= valor
            print('-- Saque autorizado! Operação realizada com sucesso. --')
            return True
        else:
            print('-- Saque não autorizado! Valor inválido. --')
        return False
    
    def depositar(self, valor):
        valor_de_deposito_valido = valor > 0

        if valor_de_deposito_valido:
            self._saldo += valor
            print('-- Depósito autorizado! Operação realizada com sucesso! --')
            return True
        else:
            print('-- Depósito não autorizado! Valor inválido. --')
            return False
        