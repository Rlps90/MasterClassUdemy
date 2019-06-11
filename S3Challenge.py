#cria lista, adiciona palavra ao final e adiciona em certa posicao da lista
foods = ['banana', 'arrot', 'beef', 'potato', 'rice']

print(foods[2])

foods.append('beans')

print(foods)

foods.insert(2, 'tacos')

print(foods)
print('')

#printar varias vezes uma frase usando for

for x in range(1, 6):
    print('I am a programmer.')
print('')
#mostrar o valor quadrado de 1 a 9

contador = 0

while contador < 10:
    print(contador*contador)
    contador += 1
print('')
#usando define

def show_square():
    for x in range(1, 10):
        print(x*x)

show_square()

