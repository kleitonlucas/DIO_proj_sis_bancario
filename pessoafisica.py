from cliente import Cliente


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f'''\
            CPF:\t\t\t{self.cpf}
            Nome:\t\t\t{self.nome}
            Data de Nascimento:\t{self.data_nascimento}
            Endereço:\t\t{self.endereco}
        '''
