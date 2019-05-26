class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, {self.nome}! Você tem {self.idade} anos.'


if __name__ == '__main__':
    Renato = Pessoa(nome='Renato', idade=39)
    Luiz = Pessoa(Renato, nome='Luiz', idade=39)
    print(Luiz.cumprimentar())
    print('*'*20)

    for filho in Luiz.filhos:
        print(filho.nome)