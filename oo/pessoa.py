class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, {self.nome}! Você tem {self.idade} anos.'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - OLHOS {cls.olhos}'


if __name__ == '__main__':
    Renato = Pessoa(nome='Renato', idade=39)
    Luiz = Pessoa(Renato, nome='Luiz', idade=39)
    print(Luiz.cumprimentar())
    print('*'*20)

    print(id(Renato.olhos), id(Luiz.olhos), id(Pessoa.olhos))
    print('*'*20)

    print(Renato.olhos)
    print('*'*20)

    for filho in Luiz.filhos:
        print(filho.nome)

    print('*'*20)
    print(Pessoa.metodo_estatico(), Luiz.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), Luiz.nome_e_atributos_de_classe())