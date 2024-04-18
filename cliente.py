class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 10:
            print('\n-- Você atingiu o limite de tansações diárias. --')
            return
        
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
