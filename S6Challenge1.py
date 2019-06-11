#Write Python code which accepts name of a product and in turn returns their respective prices.
#Make sure to use dictionaries to store products and their respective prices.
#The dictionary should include at least 5 elements.

products = {'Apple': 1.00, 'Game': 60.00, 'Soap': 2.00, 'Beer': 3.00, 'Rice': 10.00}

def user_pick(products):
    print('Please choose:')
    for idx, element in enumerate(products):
        print("{}) {}".format(idx+1, element))
    i = input('Enter a number: ')
    print(products.get(i))

    try:
        if 0 < int(i) <= len(products):
            return int(i)
    except:
        pass
    return None

user_pick(products)

'''
if choice in products:
    print(products.get(choice))
else:
    print('Invalid product.')
'''


