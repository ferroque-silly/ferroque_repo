pizzas = ['cheese', 'pepperoni', 'veggie']
friend_pizzas = pizzas[:]

pizzas.append('sausage')
friend_pizzas.append('mushroom')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza.title())

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza.title())