#import importlib

"""
Você deve criar uma classe Carro que vai possuir 2 atributos compostos por outras 2 classes:

1 - Motor
2 - Direção

O Motor terá a responsabilidade de controlar a velocidade. Ele oferece os seguintes atributos:

1 - Atributo de dado Velocidade
2 - Método Acelerar, que incrementa a velocidade em 1 unidade
3 - Método Frear, que decrementa a velocidade em 2 unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:

1 - Valor da direção com os possíveis valores: Norte, Sul, Leste, Oeste
2 - Método Girar à Direita
3 - Método Girar à Esquerda

        N

    O       L

        S

    Exemplo:
    >>> # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0


    >>> # Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'


    >>> carro = Carro (direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0


    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Sul'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Oeste'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Sul'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
"""


NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direcao():
    GIRAR_A_DIREITA = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    GIRAR_A_ESQUERDA = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.GIRAR_A_DIREITA[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.GIRAR_A_ESQUERDA[self.valor]


class Motor():
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade = max(0, self.velocidade - 2)


class Carro():
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

