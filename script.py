# Your code below:
# Make Some Pizzas
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza" )

pizza_and_prices = list(zip(prices, toppings))
print(pizza_and_prices)

# Sorting and Slicing Pizzas
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
pizza_and_prices.pop()
pizza_and_prices.insert(4, [2.5, "peppers"])
# print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]
print("THREE CHEAPEST PIZZA:")
print(three_cheapest)

