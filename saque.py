from transacao import Transacao


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao_autorizada = conta.sacar(self.valor)

        if transacao_autorizada:
            conta.historico.adicionar_transacao(self)
