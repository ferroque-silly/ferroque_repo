sandwich_orders = ['italian', 'pastrami', 'reuben', 'pastrami', 'tuna', 'buffalo chicken', 'pastrami', 'meatball']
finished_sandwiches = []

print("Alert: The deli has run out of pastrami supplies.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	current_order = sandwich_orders.pop()

	print(f"I am making your delicious {current_order.title()} sandwich.")
	finished_sandwiches.append(current_order)

print("\nThe following sandwiches have been prepared:")
for finished_sandwich in finished_sandwiches:
	print(f"{finished_sandwich.title()} sandwich")