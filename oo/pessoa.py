class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá, {self.nome}! Você tem {self.idade} anos.'


if __name__ == '__main__':
    p = Pessoa('Renato', 39)
    print(p.cumprimentar())