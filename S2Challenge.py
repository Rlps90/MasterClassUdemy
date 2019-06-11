
amount = input("Type the amount: ")
years = input('How many years to invest: ')
rate = input('What is the rate of interest: ')

total = int(amount)*int(years)*(int(rate)/100)

print("The final amount will be: ", int(amount) + total)