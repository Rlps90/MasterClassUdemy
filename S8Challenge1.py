''' Criar uma superclasse Computer com subclasses desktop e laptop e pegar e mostrar informacoes'''

class Computer:

    def __init__(self, memory, processor):
        self.memory = memory
        self.processor = processor

    def get_specs(self):
        print('Type in computer specs')
        self.memory = input('Type computers memory size: ')
        self.processor = input('Type computers processor: ')

    def display_specs(self):
        print('Computer specs:')
        print('Memory: ' + self.memory)
        print('Processor: ' + self.processor)

'''Classes com heranca'''

class Desktop(Computer):

    def __init__(self, gpu):
        self.gpu = gpu

    def get_gpu(self):
        self.gpu = input('What is desktops GPU? ')

    def display_gpu(self):
        print('GPU: ' + self.gpu)

class Laptop(Computer):

    def __init__(self, weight):
        self.weight = weight

    def get_weight(self):
        self.weight = input('What is laptops weight? ')

    def display_weight(self):
        print('Weight: ' + self.weight)

'''Teste'''

Computer1 = Desktop('')
Computer1.get_specs()
Computer1.get_gpu()
Computer1.display_specs()
Computer1.display_gpu()

Computer2 = Laptop('')
Computer2.get_specs()
Computer2.get_weight()
Computer2.display_specs()
Computer2.display_weight()


