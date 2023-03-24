class Pessoa:
    def __init__(self, *filhos, nome=None, idade=36):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def descricao_cliente(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')

if __name__ == '__main__':
    cliente = Pessoa('Pavuna', 36)
    print(cliente.descricao_cliente())