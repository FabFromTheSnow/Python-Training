#list training
#https://www.codecademy.com/courses/learn-python-3/projects/python-lens-slice
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

print(toppings)

Prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = Prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)
print(num_pizzas)

print("we sell" , num_pizzas , "different kinds of pizza!" )

pizza_and_prices2 = []

for x in range(0, len(toppings)):
    pizza_and_prices2.append([Prices[x], toppings[x]])
    

pizza_and_prices2.sort()
print(pizza_and_prices2)

cheapest_pizza = pizza_and_prices2[0][1]

print('\n'+ cheapest_pizza)


Priciest_pizza = pizza_and_prices2[-1][1]
print(Priciest_pizza)

pizza_and_prices2.remove([7, "anchovies"])
print(pizza_and_prices2)

pizza_and_prices2.append([2.5, "peppers"])
pizza_and_prices2.sort()

three_cheapest = [pizza_and_prices2[0][1], pizza_and_prices2[1][1], pizza_and_prices2[2][1]]

print("the three cheapest are", three_cheapest)

