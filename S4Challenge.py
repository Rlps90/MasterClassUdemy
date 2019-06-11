#calculadora de IMC

def body_mass_index(w, h):
    return w/(h**2)

w = float(input('What is your wheight?\n'))
h = float(input('What is your height?\n'))

result = body_mass_index(w, h)
print('Your Body Mass Index is: ' + str(result))

