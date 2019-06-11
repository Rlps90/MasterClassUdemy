''' atribuir 10% de desconto a um produto e mais 5% se for cliente regular '''

def discount(price):
    return price*0.9

def regular_client_discount(new_price):
    new_price = new_price * 0.95
    return new_price

product_price = 100

print(regular_client_discount(discount(product_price)))


