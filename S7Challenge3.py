
def discount(x):
    return x * 0.90


product_prices = [10, 20, 30, 40, 50]

result = list(map(discount, product_prices))
print(result)
