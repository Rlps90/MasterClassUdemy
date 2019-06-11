'''Usando sobrecarga de operador, fazer um operador de multiplicacao agir como adicao'''

class Multiplier:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return x

number_a = Multiplier(4)
number_b = Multiplier(5)
print(number_a * number_b)